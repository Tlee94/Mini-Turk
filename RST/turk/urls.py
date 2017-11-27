from django.conf.urls import url
from . import views

app_name = 'turk'

urlpatterns = [
    # main page - list of jobs
    url(r'^$', views.index, name='index'),

    # register page
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # login page
    url(r'^login_user/$', views.login_user, name='login_user'),

    # logout page
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # profile page
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.detail, name='detail'),

    # job description page
    url(r'^profile/(?P<user_id>[0-9]+)/job/(?P<job_id>[0-9]+)/$', views.job_description, name='job_description'),

    # create job page
    url(r'^profile/(?P<user_id>[0-9]+)/create_job/$', views.create_job, name='create_job'),

    # update profile page
    url(r'^profile/(?P<user_id>[0-9]+)/UpdateProfile/(?P<pk>[0-9]+)$', views.UpdateProfile.as_view(),
        name='update_profile'),

    # delete job
    url(r'^profile/(?P<user_id>[0-9]+)/DeleteJob/(?P<pk>[0-9]+)/delete/$', views.JobDelete.as_view(),
        name='delete_job'),

    # form to superuser page
    url(r'^profile/(?P<user_id>[0-9]+)/ftsu/$', views.form_to_superuser, name='form_to_superuser'),

]