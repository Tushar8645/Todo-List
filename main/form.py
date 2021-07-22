from django import forms
from django.forms import widgets
from main.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
