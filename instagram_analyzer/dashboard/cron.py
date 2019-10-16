from django.utils import timezone
from dashboard.models import AccountSummary
import instagram_explore as ie

def scrape_instagram():

    key = 'account_name'
    name_list = AccountSummary.objects.all().values_list(key, flat=True).order_by(key).distinct()

    for name in name_list:

        response  = ie.user(name)

        posts     = response.data['edge_owner_to_timeline_media']['count']
        followers = response.data['edge_followed_by']['count']
        follows   = response.data['edge_follow']['count']

        posts        = int(posts)
        followers    = int(followers)
        follows      = int(follows)
        scrape_date  = timezone.now(),

        rows = AccountSummary.objects.filter(account_name = name)

        for row in rows:
            print(vars(row))
            a = AccountSummary(
                id          = row.id,
                user_id     = row.user_id,
                posts       = posts,
                followers   = followers,
                follows     = follows,
                scrape_date = scrape_date
            )
            a.save()
