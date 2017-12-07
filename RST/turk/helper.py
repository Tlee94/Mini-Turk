from .models import DeveloperChosenForJob
from datetime import datetime, timedelta
from django.utils import timezone

def get_lowest_bid(job):
    bid_list = job.bidder_set.all()
    count = job.bidder_set.count()

    if count > 0:
        lowest_bid = bid_list[0].price
        for bid in bid_list:
            if bid.price < lowest_bid:
                lowest_bid = bid.price
        job.lowest_bid = lowest_bid
        job.save()


def assign_developer(user, job, bidder_user, bidder, initial_payment):
    bidder_user.profile.money += initial_payment
    user.profile.money -= initial_payment
    bidder.isHired = True
    job.is_open = False
    job.save()
    bidder.save()
    bidder_user.profile.save()
    user.profile.save()
    developer = DeveloperChosenForJob(job=job, user=bidder_user)
    developer.save()

def give_trophy(profile):
    # Give trophy and revoke if they cant maintain

    # deliver before deadline and receive rating >=4 for >=5 demands, give early bird
    if((profile.num_early >= 5) and (profile.average_rating >=4)):
        profile.honor_Early_Bird = True
        profile.save()
    else:
        profile.honor_Early_Bird = False
        profile.save()

    # avg rating >=4 for >=10 demand, give hard worker
    if((profile.average_rating >=4) and (profile.rating_count >=10)):
        profile.honor_Hard_Worker = True
        profile.save()
    else:
        profile.honor_Hard_Worker = False
        profile.save()

    # made more than $1M from demands, give MILLIONAIRE!
    if(profile.money_earned > 1000000):
        profile.honor_MILLIONAIRE = True
        profile.save()

    # post >10 demands, give job supplier
    if(profile.num_post > 10):
        profile.honor_Job_Supplier = True
        profile.save()

    # dev worked on >=20 demands, give veteran
    if(profile.rating_count >= 20):
        profile.honor_Veteran = True
        profile.save()

    # clients got no bid on >10 expired demands, give toohardman
    if(profile.num_post_ex > 10):
        profile.honor_toohardman = True
        profile.save()

    # users with 'Tim' in name, give Cold-Headed-Tim
    if(profile.user.first_name == 'Tim'):
        profile.honor_Cold_Headed_Tim = True
        #print(profile.user.first_name)
        profile.save()
    else:
        profile.honor_Cold_Headed_Tim = False
        #print(profile.user.first_name)
        profile.save()

    # Get Age of Account
    a = timezone.now() - timezone.timedelta(hours=5) # -5 hrs b/c wrong timezone
    b = profile.acc_created
    c=a-b
    diff_day=c.days

    # >= 90 days, award Normie
    if(profile.honor_Novice == True):
        if(diff_day >= 90):
            # print('NORMIE')
            profile.honor_Novice = False
            profile.honor_Normie = True
            profile.save()

    # >= 365 days, award General
    if(profile.honor_Normie == True):
        if(diff_day >= 365):
            # print('GENERAL')
            profile.honor_Normie = False
            profile.honor.General = True
            profile.save()

    # 90+ days user + No activity, award Lurker
    if(diff_day >= 90):
        if(profile.rating_count == 0):
            profile.honor_Lurker = True
            profile.save()
        else:
            profile.honor_Lurker = False
            profile.save()


def warn_user(profile):
    # Poor Performance
    if(profile.rating_count >= 5):
        if(profile.average_rating <= 2):
            profile.warn_poor = True
            profile.save()
        else:
            profile.warn_poor = False
            profile.save()

    # Irresponsible evaluations to others
    if(profile.rating_count >= 8):
        if((profile.avg_give_rating < 2) or (profile.avg_give_rating >4)):
            profile.warn_eval = True
            profile.save()
        else:
            profile.warn_eval = False
            profile.save()

    if((profile.warn_poor == True) and (profile.warn_eval == True) and (profile.warn_final == False)):
        profile.warn_final = True
        profile.save()
        print('Final warning:', profile.warn_final)

    # # Time to get tossed out :) for being warned twice hehexd
    # if(profile.warn_final == True):
    #     user.is_active = False
    #     user.save()
    #     profile.isBlackListed = True
    #     profile.save()
    #     print('byebye')

def ban(profile,user):
    if (profile.warn_final == True):
        user.is_active = False
        user.save()
        profile.isBlackListed = True
        profile.save()
        print('byebye')


def update_rate_db(rating, job):
    job.user.profile.total_rating += rating
    job.user.profile.rating_count += 1
    job.user.profile.average_rating = (job.user.profile.total_rating / job.user.profile.rating_count)
    job.user.profile.save()
    job.is_rated = True
    job.save()
    print("job total rating: ", job.user.profile.total_rating)
    print("job rating count: ", job.user.profile.rating_count)
    print("job avereage rating: ", job.user.profile.average_rating)


