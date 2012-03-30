from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.template import RequestContext
from models import *
from forms import VolunteerRegForm, TreeByOwnerForm, TreeReviewForm
from maps import geo_code

def home(request):
    volunteers = Volunteer.objects.all()
    trees = Tree.objects.all()
    return render_to_response("home.html", {'volunteers':volunteers, 'trees':trees}, context_instance=RequestContext(request))

def tree_list(request):
    trees = Tree.objects.all()
    return render_to_response("trees.html", {'trees':trees}, context_instance=RequestContext(request))

def spotted_tree_list(request):
    trees = SpottedTree.objects.all()
    for tree in trees:
        tree.lat = geo_code(tree.address.address, tree.address.city, tree.address.state, tree.address.zip)[0]
        tree.lng = geo_code(tree.address.address, tree.address.city, tree.address.state, tree.address.zip)[1]
        tree.save()
    return render_to_response("spotted_trees.html", {'trees':trees}, context_instance=RequestContext(request))
    
def harvest_detail(request, entry_id):
    harvest = get_object_or_404(Harvest, pk=entry_id)
    return render_to_response("harvest_detail.html", {'harvest':harvest}, context_instance=RequestContext(request))

def planned_harvests(request):
    harvests = Harvest.objects.all()
    return render_to_response("planned_harvests.html", {'harvests':harvests}, context_instance=RequestContext(request))
    

def review(request, entry_id):
    tree = get_object_or_404(Tree, pk=entry_id)
    if request.method == 'POST':
        form = TreeReviewForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            pounds = form.cleaned_data['pounds']
            issues = form.cleaned_data['issues']
            new_review = PostHarvestTree(date=date, pounds=pounds, issues=issues)
            new_review.save()
            tree.harvests.add(new_review)
            return redirect("/tree_review/"+entry_id+"/")
    else:
        form = TreeReviewForm()
    return render_to_response("tree_review.html", {'form':form, 'tree':tree}, context_instance=RequestContext(request))
        

    return render_to_response("tree_review.html", {'tree':tree}, context_instance=RequestContext(request))
    

def tree_by_owner(request):
    if request.method == 'POST':
        form = TreeByOwnerForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            print type
            owner = form.cleaned_data['owner']
            owner_email = form.cleaned_data['owner_email']
            owner_phone = form.cleaned_data['owner_phone']
#            who_will_harvest = form.cleaned_data['who_will_harvest']
            yard_location = form.cleaned_data['yard_location']
            height = form.cleaned_data['height']
            age = form.cleaned_data['age']
            production = form.cleaned_data['production']
            sprayed = form.cleaned_data['sprayed']
            ripen_month = form.cleaned_data['ripen_month']
            reference = form.cleaned_data['refererence']
            reference_email = form.cleaned_data['reference_email']
            comments = form.cleaned_data['comments']
            lat=geo_code(request.POST["address"], request.POST["city"], request.POST['state'], request.POST['zip'])[0]
            lng=geo_code(request.POST["address"], request.POST["city"], request.POST['state'], request.POST['zip'])[1]            
            print request.POST['address']
            print request.POST['city']
            new_address = Address(address=request.POST["address"], city=request.POST["city"], state=request.POST['state'], zip=request.POST['zip'])
            print new_address
            new_address.save()
            new_tree = Tree(type=type, address=new_address, owner=owner, owner_email=owner_email, owner_phone=owner_phone,
                            yard_location=yard_location, height=height, age=age, production=production, sprayed=sprayed,ripen_month=ripen_month,
                            refererence=reference, reference_email=reference_email, comments=comments, lat=lat, lng=lng)
            new_tree.save()
            return redirect("/tree_list/")
    else:
        form = TreeByOwnerForm()
    return render_to_response("tree_by_owner.html", {'form':form}, context_instance=RequestContext(request))

def volunteer_registration(request):
    if request.method == 'POST':
        form = VolunteerRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            group = form.cleaned_data['group']
            health = form.cleaned_data['health']
            emergency_contact_name = form.cleaned_data['emergency_contact_name']
            emergency_contact_phone = form.cleaned_data['emergency_contact_phone']
            minor = form.cleaned_data['minor']
            minor_contact = form.cleaned_data['minor_contact']
            newsletter = form.cleaned_data['newsletter']
            user = User.objects.create_user(username, email, password)
            volunteer = Volunteer(user=user,first_name=first_name, last_name=last_name, phone=phone, group=group, health=health,
                                  emergency_contact_name=emergency_contact_name, emergency_contact_phone=emergency_contact_phone, 
                                  minor = minor, minor_contact=minor_contact, newsletter=newsletter)
            volunteer.save()
            for j in form.cleaned_data['job']:
                volunteer.job.add(j)
                volunteer.save()
            for r in form.cleaned_data['referer']:
                volunteer.referer.add(r)
                volunteer.save()
            return redirect("/")
    else:
        form = VolunteerRegForm()
    return render_to_response("volunteer_registration.html", {'form':form}, context_instance=RequestContext(request))
