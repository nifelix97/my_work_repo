from django import forms
from django.forms import ModelForm
from .models import event


class eventForm(ModelForm):
    class Meta:
        model = event
        fields = ('title', 'description', 'start_date', 'end_date', 'location', 'name', 'email', 'photo')