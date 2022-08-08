from django import forms

from todoapp.models import task

class todoform(forms.ModelForm):
    class Meta:
        model=task
        fields = ['name','priority','date']


