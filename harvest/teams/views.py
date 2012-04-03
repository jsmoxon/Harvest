from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.template import RequestContext
from trees.models import *
from trees.maps import geo_code
from forms import CreateHarvestForm, HarvestSignupForm, HarvestReviewForm
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import authenticate, login

def hello(request):
    return render_to_response("hello.html")

#select date, city and agency
def create(request):
    ripe_trees = Tree.objects.filter(ripe=True)
    if request.method == 'POST':
        form = CreateHarvestForm(request.POST)
#        form.fields['trees'].queryset = Tree.objects.filter(ripe=True)
        if form.is_valid():
            new_harvest = form.save()
            subject = "We're Harvesting Fruit on "+str(form.cleaned_data['date'])
            message = "Hello! The Urban Farmers will be harvesting fruit in Lafayette on "+str(form.cleaned_data['date'])+". We would love it if you could come to volunteer. If you would like to volunteer please signup at http://localhost:8000/teams/signup/"+str(new_harvest.id)
            to = []
            volunteers = Volunteer.objects.all()
            if volunteers != None:
                for vol in volunteers:
                    to.append(vol.user.email)
                email = EmailMessage(subject, message, "remindr.email@gmail.com", [], to)
                email.send()
            tree_list = request.POST.getlist('tree_list')
            for t in tree_list:
                new_harvest.trees.add(Tree.objects.get(pk=t))
                new_harvest.save()
            return redirect("/teams/harvest_dash/"+str(new_harvest.id))
    else:
        form = CreateHarvestForm()
 #       form.fields['trees'].queryset =Tree.objects.filter(ripe=True)
    return render_to_response("create.html", {'form':form, 'ripe_trees':ripe_trees}, context_instance=RequestContext(request))

def planned_harvests(request):
    harvests = Harvest.objects.all()
    return render_to_response("planned_harvests.html", {'harvests':harvests}, context_instance=RequestContext(request))

def harvest_detail(request, entry_id):
    harvest = get_object_or_404(Harvest, pk=entry_id)
    return render_to_response("harvest_detail.html", {'harvest':harvest}, context_instance=RequestContext(request))

# this function needs cleaning and data validation but i wnated to get something working
def harvest_review(request, entry_id):
    harvest = get_object_or_404(Harvest, pk=entry_id)
    if request.method == 'POST':
        form = HarvestReviewForm(request.POST)
        for t in request.POST.getlist('tree_list'):
            import datetime
            update_tree = Tree.objects.get(pk=str(t))
            post_tree = PostHarvestTree(date=harvest.date, pounds=request.POST[str(t)])
            post_tree.save()
            update_tree.harvests.add(post_tree)
            update_tree.save()
        print request.POST.getlist('volunteer_list')
        for v in request.POST.getlist('volunteer_list'):
            new_comment = Comment(volunteer=Volunteer.objects.get(pk=str(v)), comment="I showed up at the event!")
            new_comment.save()
            print new_comment
            harvest.comment.add(new_comment)
            harvest.save()
        return redirect('/')
    else:
        form = HarvestReviewForm()
    return render_to_response("harvest_review.html", {'form':form,'harvest':harvest}, context_instance=RequestContext(request))


def signup(request, entry_id):
    """A form that lets a volunteers signup to volunteer on a certain day"""
    harvest = get_object_or_404(Harvest, pk=entry_id)
    if request.method == 'POST':
        form = HarvestSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            harvest = get_object_or_404(Harvest, pk=entry_id)
            volunteer = Volunteer.objects.get(user=user)
            harvest.volunteers.add(volunteer)
            print form.cleaned_data['comments']
            new_comment = Comment(volunteer=volunteer, comment=form.cleaned_data['comments'])
            new_comment.save()
            harvest.comment.add(new_comment)
            return HttpResponse("Thanks! You're signed up.")
    else:
        form = HarvestSignupForm()
    return render_to_response("signup.html", {'form':form, 'harvest':harvest}, context_instance=RequestContext(request))

        
    
