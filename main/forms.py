from django import forms
from django.http import request
import django.core.validators
from django.contrib import messages
from .utility import Dzialy, liczbyrzeczywiste


class BaseForm(forms.Form):
    trudnosci = ((1,'Łatwy'),(2,'Średni'),(3,'Trudny'))
    dzial  = forms.ChoiceField(choices=Dzialy, initial="liczbyrzeczywiste")
    tematy = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=liczbyrzeczywiste)
    trudnosc = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=trudnosci)
    
class TestForm(BaseForm):
    liczbazad = forms.IntegerField(initial=6, max_value=10, min_value=1)

class ContactForm(BaseForm):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'style':'resize:none'}))