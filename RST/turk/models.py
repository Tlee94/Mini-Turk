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

    resume = models.FileField()
    sample_work_or_bussiness_credential = models.FileField()


    RATING_CHOICES=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = models.FloatField(choices=RATING_CHOICES, default=5)

    average_rating = models.FloatField(default=0)       # average of rating RECEIVED by others
    rating_count = models.IntegerField(default=0)       # count of rating RECEIVED by others
    total_rating = models.FloatField(default=0)         # total rating RECEIVED by others

    avg_give_rating = models.FloatField(default=0)      # average of rating GIVEN to others
    total_give_rating = models.FloatField(default=0)    # total of rating GIVEN to others
    total_give_count = models.FloatField(default=0)     # count of rating GIVEN to others

    money = models.FloatField(default=0)

    POSITION_CHOICES=(
        ('Temporary', 'Temporary'),
        ('Client', 'Client'),
        ('Developer', 'Developer'),
    )
    position = models.CharField(max_length=9, choices=POSITION_CHOICES, default='Temporary')

    DESIRED_POSITION_CHOICES=(
        ('Client', 'Client'),
        ('Developer', 'Developer'),
    )

    desired_position = models.CharField(max_length=9, choices=DESIRED_POSITION_CHOICES, default='Client')


    profile_picture = models.ImageField(default='default.png')
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

    honor_Early_Bird = models.BooleanField(default=False)
    honor_Hard_Worker = models.BooleanField(default=False)
    honor_MILLIONAIRE = models.BooleanField(default=False)
    honor_Job_Supplier = models.BooleanField(default=False)
    honor_Veteran = models.BooleanField(default=False)
    honor_toohardman = models.BooleanField(default=False)
    honor_Cold_Headed_Tim = models.BooleanField(default=False)
    honor_Novice = models.BooleanField(default=True)
    honor_Normie = models.BooleanField(default=False)
    honor_General = models.BooleanField(default=False)
    honor_Lurker = models.BooleanField(default=False)


    num_early = models.IntegerField(default=0)      # number of time dev delivered early
    money_earned = models.FloatField(default=0)     # amount of money dev made
    num_post = models.IntegerField(default=0)       # number of total posts client posted
    num_post_ex = models.IntegerField(default=0)    # number of expired posts client posted

    acc_created = models.DateTimeField(default=datetime.now())   # date of when acc made

    warn_poor = models.BooleanField(default=False)  # avg rating <=2 for >=5 projects
    warn_eval = models.BooleanField(default=False)  # avg rating to others <2 or >4 for >=8 projects
    warn_money = models.BooleanField(default=False) # not enough money to pay
    warn_final = models.BooleanField(default=False) # final warning, next login = gg

    def __str__(self):
        return self.name


class Job(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    job_price = models.FloatField(default=0)

    is_complete = models.BooleanField(default=False) # job submitted
    is_late = models.BooleanField(default=False)
    is_rated = models.BooleanField(default=False)

    is_open = models.BooleanField(default=True) # Job is still open for bid
    lowest_bid = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)], default=0)
    bid_deadline = models.DateTimeField(default=datetime.now()+timedelta(7))
    job_deadline = models.DateTimeField(default=datetime.now()+timedelta(21))

    def __str__(self):
        return self.job_title

# list of ppl who bid on job
class Bidder(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    price = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(100000)], default=1)
    isHired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.price)


class DeveloperChosenForJob(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_rated = models.BooleanField(default=False)


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
        ('Poor Performance', 'Poor Performance'),
        ('Bad Evaluator','Bad Evaluator'),
        ('Not Enough Funds','Not Enough Funds'),
        ('Jobs', 'Jobs'),
    )
    reason = models.CharField(max_length=30, choices=MESSAGE_REASONS, default='Warnings')

    def __str__(self):
        return self.title


class JobSubmission(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=1)
    submission = models.TextField()
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = models.FloatField(choices=RATING_CHOICES, default=5)
    reason = models.TextField()

    def __str__(self):
        return self.submission


class ClientRateForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=1)
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = models.FloatField(choices=RATING_CHOICES, default=5)
    reason = models.TextField()

    def __str__(self):
        return self.reason


class ProtestWarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reason = models.TextField()

    def __str__(self):
        return self.reason

