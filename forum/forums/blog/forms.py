from django import forms

class Searchform(forms.Form):
    query = forms.CharField(label='search',max_length=100)
