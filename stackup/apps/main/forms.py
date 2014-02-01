from django import forms

class SalaryForm(forms.Form):
    salary = forms.IntegerField()
