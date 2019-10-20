from django.utils import timezone
from django.db import IntegrityError
from dashboard.models import AccountSummary
from dashboard.models import AccountFollowers
from dashboard.models import AccountFollows
from dashboard import scrape
from json.decoder import JSONDecodeError

def scrape_instagram():

    key = 'account_name'
    name_list = AccountSummary.objects.all().values_list(key, flat=True).order_by(key).distinct()

    for name in name_list:
        try:
            scrape.scrape_instagram(name)
        except JSONDecodeError:
            print("Account Not Found: " + name)
            continue
