from django.contrib.auth.models import User
from django import forms
from .models import Profile, Job, Bidder


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['job_title', 'job_description']


class BidForm(forms.ModelForm):

    class Meta:
        model = Bidder
        fields = ['price']

