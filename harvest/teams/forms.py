from django.forms import ModelForm
from trees.models import *
from django import forms

class CreateHarvestForm(ModelForm):
    class Meta:
        model = Harvest
        exclude = ('volunteers', 'comment')
        widgets = {
            'trees': forms.CheckboxSelectMultiple(),
            }

class HarvestSignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    yes= forms.BooleanField()
    comments = forms.CharField(widget=forms.Textarea())
