from django import forms
from.models import LoginMatch,Tasktodo


class Formfield(forms.ModelForm):
    class Meta:
        model = LoginMatch
        fields = ['username', 'password']


class Taskfield(forms.ModelForm):
    class Meta:
        model = Tasktodo
        fields = ['Title', 'Task']
