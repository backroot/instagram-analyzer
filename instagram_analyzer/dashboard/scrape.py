from django.utils import timezone
from django.db import IntegrityError
from django.db import transaction
from dashboard.models import AccountSummary
from dashboard.models import AccountFollowers
from dashboard.models import AccountFollows
from json.decoder import JSONDecodeError
import datetime
import time
import instagram_explore as ie

def scrape_instagram(account_name):

    scrape_date  = timezone.now()
    scrape_date  = datetime.datetime.strftime(scrape_date, '%Y-%m-%d')

    today = scrape_date.split('-')
    year  = int(today[0])
    month = int(today[1])
    day   = int(today[2])

    response = ie.user(account_name)
    time.sleep(0.5)

    posts           = response.data['edge_owner_to_timeline_media']['count']
    followers       = response.data['edge_followed_by']['count']
    follows         = response.data['edge_follow']['count']
    profile_pic_url = response.data['profile_pic_url']

    data = {
        "scrape_date":     scrape_date,
        "posts":           int(posts),
        "followers":       int(followers),
        "follows":         int(follows),
        "profile_pic_url": profile_pic_url
    }

    rows = AccountSummary.objects.filter(account_name = account_name)

    if 0 < rows.count():
        insert_or_update_summary(rows, data)
    else:
        a = AccountSummary(
            account_name    = account_name,
            scrape_date     = data["scrape_date"],
            posts           = data["posts"],
            followers       = data["followers"],
            follows         = data["follows"],
            profile_pic_url = data["profile_pic_url"]
        )
        a.save()

    followers = AccountFollowers.objects.filter(account_name = account_name).first()
    follows   = AccountFollows.objects.filter(account_name = account_name).first()

    if (followers == None):
        AccountFollowers(account_name = account_name).save()

    if (follows == None):
         AccountFollows(account_name = account_name).save()

    followers_month = []
    follows_month   = []

    for i in range(2):
        a = AccountSummary.objects.filter(
            account_name       = account_name,
            scrape_date__year  = year,
            scrape_date__month = month - i
        ).order_by('-scrape_date').first()
        if (a):
            followers_month.append(a.followers)
            follows_month.append(a.follows)
        else:
            followers_month.append(None)
            follows_month.append(None)

    b = AccountFollowers.objects.get(account_name = account_name)

    b.profile_pic_url = profile_pic_url
    b.month_now       = followers_month[0]
    b.month_prev      = followers_month[1]
    if followers_month[0] is not None and followers_month[1] is not None:
        b.month_diff  = followers_month[0] - followers_month[1]

    c = AccountFollows.objects.get(account_name = account_name)
    c.profile_pic_url = profile_pic_url
    c.month_now       = follows_month[0]
    c.month_prev      = follows_month[1]
    if follows_month[0] is not None and follows_month[1] is not None:
        c.month_diff      = follows_month[0] - follows_month[1]

    followers_days = []
    follows_days   = []
    
    for i in range(9):
        a = AccountSummary.objects.filter(
            account_name = account_name,
            scrape_date__year = year,
            scrape_date__month = month,
            scrape_date__day = day - i
        ).first()
        if (a):
            followers_days.append(a.followers)
            follows_days.append(a.follows)
        else:
            followers_days.append(None)
            follows_days.append(None)

    b.today      = followers_days[0]
    b.prev_one   = followers_days[1]
    b.prev_two   = followers_days[2]
    b.prev_three = followers_days[3]
    b.prev_four  = followers_days[4]
    b.prev_five  = followers_days[5]
    b.prev_six   = followers_days[6]
    b.prev_seven = followers_days[7]
    b.prev_eight = followers_days[8]

    if followers_days[0] is not None and followers_days[1] is not None:
        b.today_diff      = followers_days[0] - followers_days[1]
    if followers_days[1] is not None and followers_days[2] is not None:
        b.prev_one_diff   = followers_days[1] - followers_days[2]
    if followers_days[2] is not None and followers_days[3] is not None:
        b.prev_two_diff   = followers_days[2] - followers_days[3]
    if followers_days[3] is not None and followers_days[4] is not None:
        b.prev_three_diff = followers_days[3] - followers_days[4]
    if followers_days[4] is not None and followers_days[5] is not None:
        b.prev_four_diff  = followers_days[4] - followers_days[5]
    if followers_days[5] is not None and followers_days[6] is not None:
        b.prev_five_diff  = followers_days[5] - followers_days[6]
    if followers_days[6] is not None and followers_days[7] is not None:
        b.prev_six_diff   = followers_days[6] - followers_days[7]
    if followers_days[7] is not None and followers_days[8] is not None:
        b.prev_seven_diff = followers_days[7] - followers_days[8]

    b.save()

    c.today      = follows_days[0]
    c.prev_one   = follows_days[1]
    c.prev_two   = follows_days[2]
    c.prev_three = follows_days[3]
    c.prev_four  = follows_days[4]
    c.prev_five  = follows_days[5]
    c.prev_six   = follows_days[6]
    c.prev_seven = follows_days[7]
    c.prev_eight = follows_days[8]

    if follows_days[0] is not None and follows_days[1]:
        c.today_diff      = follows_days[0] - follows_days[1]
    if follows_days[1] is not None and follows_days[2]:
        c.prev_one_diff   = follows_days[1] - follows_days[2]
    if follows_days[2] is not None and follows_days[3]:
        c.prev_two_diff   = follows_days[2] - follows_days[3]
    if follows_days[3] is not None and follows_days[4]:
        c.prev_three_diff = follows_days[3] - follows_days[4]
    if follows_days[4] is not None and follows_days[5]:
        c.prev_four_diff  = follows_days[4] - follows_days[5]
    if follows_days[5] is not None and follows_days[6]:
        c.prev_five_diff  = follows_days[5] - follows_days[6]
    if follows_days[6] is not None and follows_days[7]:
        c.prev_six_diff   = follows_days[6] - follows_days[7]
    if follows_days[7] is not None and follows_days[8]:
        c.prev_seven_diff = follows_days[7] - follows_days[8]

    c.save()

def insert_or_update_summary(rows, data):

    for row in rows:

        a = AccountSummary(
            account_name    = row.account_name,
            scrape_date     = data["scrape_date"],
            posts           = data["posts"],
            followers       = data["followers"],
            follows         = data["follows"],
            profile_pic_url = data["profile_pic_url"]
        )
        try:
            a.save()
        except IntegrityError:
            b = AccountSummary.objects.get(id = row.id)
            if str(b.scrape_date) == data["scrape_date"]:
                b.posts           = data["posts"]
                b.followers       = data["followers"]
                b.follows         = data["follows"]
                b.profile_pic_url = data["profile_pic_url"]
                b.save()
 
