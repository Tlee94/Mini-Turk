from django.conf.urls import url
from . import views

app_name = 'turk'

urlpatterns = [
    # main page - list of jobs
    url(r'^$', views.index, name='index'),

    # register page
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # profile page
    url(r'^(?P<profile_id>[0-9]+)/$', views.detail, name='detail'),

    # job description page
    url(r'^(?P<profile_id>[0-9]+)/job/(?P<job_id>[0-9]+)/$', views.job_description, name='job_description'),

    # create job page
    url(r'^(?P<profile_id>[0-9]+)/create_job/$', views.create_job, name='create_job'),
]