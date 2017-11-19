from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


def index(request):
    all_profiles = Profile.objects.all()
    context = {
        'all_profiles': all_profiles,
    }
    return render(request, 'turk/index.html', context)


def detail(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        raise Http404("Profile Does Not Exist")
    return render(request, 'turk/detail.html',  {'profile': profile})
