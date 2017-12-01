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

