from django.shortcuts import render, get_object_or_404
from .models import Profile,Job


def index(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return render(request, 'turk/index.html', context)


def detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'turk/detail.html',  {'profile': profile})


def job_description(request, profile_id, job_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    job = Job.objects.get(pk=job_id)
    context = {
        'profile': profile,
        'job': job,
    }
    return render(request, 'turk/job_description.html', context)


def create_job(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'turk/create_job.html', {'profile': profile})


