from django import forms
from django.forms import ModelForm

from .models import *


class TaskModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task'}))

    class Meta:
        model = TaskModel
        fields = '__all__'
