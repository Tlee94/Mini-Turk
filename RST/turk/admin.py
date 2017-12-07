from django.contrib import admin
from .models import Profile, Job, Bidder, FormToSuperUser, DeveloperChosenForJob, Message, JobSubmission

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Bidder)
admin.site.register(FormToSuperUser)
admin.site.register(DeveloperChosenForJob)
admin.site.register(Message)
admin.site.register(JobSubmission)


