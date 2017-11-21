from django.contrib.auth.models import User
from django import forms
from .models import Profile, Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['job_title', 'job_description']