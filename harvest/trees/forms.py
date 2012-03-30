from django.forms import ModelForm
from models import *
from django import forms
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

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

class HouseForm(ModelForm):
    class Meta:
        model = House
        exclude = ('lat', 'lng')

class TreeByOwnerForm(ModelForm):
    class Meta:
        model = Tree
        exclude = ('harvests', 'house', 'ripe')

TreeFormSet = formset_factory(TreeByOwnerForm, extra=3)


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
