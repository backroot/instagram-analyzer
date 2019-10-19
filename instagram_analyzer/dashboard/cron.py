from django.utils import timezone
from django.db import IntegrityError
from dashboard.models import AccountSummary
import datetime
import instagram_explore as ie

def scrape_instagram():

    key = 'account_name'
    name_list = AccountSummary.objects.all().values_list(key, flat=True).order_by(key).distinct()
    scrape_date  = timezone.now()
    scrape_date  = datetime.datetime.strftime(scrape_date, '%Y-%m-%d')

    for name in name_list:

        response  = ie.user(name)

        posts     = response.data['edge_owner_to_timeline_media']['count']
        followers = response.data['edge_followed_by']['count']
        follows   = response.data['edge_follow']['count']

        data = {
            "scrape_date": scrape_date,
            "posts":       int(posts),
            "followers":   int(followers),
            "follows":     int(follows)
        }

        rows = AccountSummary.objects.filter(account_name = name)
        insert_or_update(rows, data)

def insert_or_update(rows, data):

    for row in rows:
        a = AccountSummary(
            user_id      = row.user_id,
            account_name = row.account_name,
            scrape_date  = data["scrape_date"],
            posts        = data["posts"],
            followers    = data["followers"],
            follows      = data["follows"]
        )
        try:
            a.save()
        except IntegrityError:
            b = AccountSummary.objects.get(id = row.id)
            if str(b.scrape_date) == data["scrape_date"]:
                b.posts     = data["posts"]
                b.followers = data["followers"]
                b.follows   = data["follows"]
                b.save()
