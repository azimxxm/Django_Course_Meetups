from django import forms
from django.forms import fields
from .models import *



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'