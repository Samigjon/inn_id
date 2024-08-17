from django import forms

class TINForm(forms.Form):
    tin = forms.CharField(label='ИНН', max_length=12)