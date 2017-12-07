from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


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
    RATING_CHOICES=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rating = models.FloatField(choices=RATING_CHOICES, default=5)
    average_rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    money = models.FloatField(default=0)
    POSITION_CHOICES=(
        ('Temporary', 'Temporary'),
        ('Client', 'Client'),
        ('Developer', 'Developer'),
    )
    position = models.CharField(max_length=9, choices=POSITION_CHOICES, default='Temporary')
    profile_picture = models.ImageField()
    interest = models.TextField()
    isBlackListed = models.BooleanField(default=False)
    INTEREST_CHOICES=(
        ('Being Human', 'Being Human'),
        ('Software Development', 'Software Development'),
        ('Video Games', 'Video Games'),
        ('Social Media', 'Social Media'),
        ('Food', 'Food'),
        ('Party', 'Party'),
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Money', 'Money'),
    )
    interest = MultiSelectField(choices=INTEREST_CHOICES, default="Being Human")
    #isClient = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    job_price = models.FloatField(default=0)
    is_complete = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True) # Job is still open for bid
    lowest_bid = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    bid_deadline = models.DateTimeField(default=datetime.now()+timedelta(7))

    def __str__(self):
        return self.job_title


class Bidder(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    price = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    isHired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.price)


class DeveloperChosenForJob(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class FormToSuperUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    writing = models.TextField()
    REASON_OPTIONS = (
        ('Not Lowest Bid', 'Not Lowest Bid'),
        ('Rating Warning', 'Rating Warning'),
        ('Protest Rating', 'Protest Rating'),
        ('Protest Warning', 'Protest Warning'),
        ('Quit The System', 'Quit The System')
    )
    reason = models.CharField(max_length=35, choices=REASON_OPTIONS, default='Not Lowest Bid')

    def __str__(self):
        return str(self.reason)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    message = models.TextField()
    MESSAGE_REASONS = (
        ('Warnings', 'Warnings'),
        ('Jobs', 'Jobs'),
    )
    reason = models.CharField(max_length=9, choices=MESSAGE_REASONS, default='Temporary')

    def __str__(self):
        return self.title
