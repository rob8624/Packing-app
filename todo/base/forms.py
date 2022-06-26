from django import forms
from .models import Box

class PackForm(forms.Form):
    pack = forms.ModelChoiceField(queryset=Box.boxes.all().order_by('number'))