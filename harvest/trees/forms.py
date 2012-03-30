from django.forms import ModelForm
from models import *
from django import forms

class VolunteerRegForm(ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    class Meta:
        model = Volunteer        
        exclude = ('user', )
        widgets = {
            'job': forms.CheckboxSelectMultiple(),
            'referer': forms.CheckboxSelectMultiple(),
        }

class TreeByOwnerForm(ModelForm):
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.CharField()
    class Meta:
        model = Tree
        exclude = ('harvests', 'spotted', 'address', 'who_will_harvest', 'lat', 'lng', 'ripe')

class SpottedTreeForm(ModelForm):
    class Meta:
        model = SpottedTree
        exclude = ('harvests', )

class CreateHarvestForm(ModelForm):
    class Meta:
        model = Harvest
        widgets = {
            'trees': forms.CheckboxSelectMultiple(),
            'volunteers': forms.CheckboxSelectMultiple(),
        }
          
class TreeReviewForm(ModelForm):
    class Meta:
        model = PostHarvestTree
