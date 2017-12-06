from .models import DeveloperChosenForJob

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








