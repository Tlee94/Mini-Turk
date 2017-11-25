from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, default=1)
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    gender = models.BinaryField(default=1) # 1 = male 0 = female
    email = models.CharField(max_length=250)
    rating = models.FloatField(default=5)
    money = models.FloatField(default=0)
    isClient = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1)
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    is_complete = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True) # Job is still open for bid
    lowest_bid = models.FloatField(default=-1)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title


class Bidder(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return str(self.price)

