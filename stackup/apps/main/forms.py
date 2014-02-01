from django import forms
from django.forms.widgets import NumberInput

class SalaryForm(forms.Form):
    salary = forms.IntegerField(required=True, widget=NumberInput(attrs={'required':'true'}))
