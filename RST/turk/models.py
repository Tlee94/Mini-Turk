from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    #gender = models.BinaryField(default=1) # 1 = male 0 = female
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    email = models.CharField(max_length=250)
    rating = models.FloatField(default=5)
    money = models.FloatField(default=0)
    POSITION_CHOICES=(
        ('Temporary', 'Temporary'),
        ('Client', 'Client'),
        ('Developer', 'Developer'),
    )
    position = models.CharField(max_length=9, choices=POSITION_CHOICES, default='Temporary')
    profile_picture = models.ImageField()
    interest = models.TextField()
    #isClient = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    is_complete = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True) # Job is still open for bid
    lowest_bid = models.FloatField(default=-1)
    bid_deadline = models.DateTimeField(default=datetime.now()+timedelta(7))

    def __str__(self):
        return self.job_title


class Bidder(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    price = models.FloatField(default=0)

    def __str__(self):
        return str(self.price)


class FormToSuperUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    writing = models.TextField()
    REASON_OPTIONS = (
        ('Not_lowest_bid', 'Not_lowest_bid'),
        ('Rating_Warning', 'Rating_Warning'),
        ('Protest_Rating', 'Protest_Rating')
    )
    reason = models.CharField(max_length=35, choices=REASON_OPTIONS, default='Not_lowest_bid')

    def __str__(self):
        return str(self.reason)
