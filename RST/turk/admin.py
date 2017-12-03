from django.contrib import admin
from .models import Profile, Job, Bidder, FormToSuperUser, DeveloperChosenForJob

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Bidder)
admin.site.register(FormToSuperUser)
admin.site.register(DeveloperChosenForJob)
