from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.db import transaction
from dashboard.models import AccountSummary
from dashboard.models import AccountFollowers
from dashboard.models import AccountFollows
from dashboard import scrape
from json.decoder import JSONDecodeError
import json
import time

def index(request):

    mode  = request.GET.get("mode", "followers")
    sort  = request.GET.get("sort", "id")
    order = request.GET.get("order", "asc")

    account = None
    if mode == "follows":
        account = AccountFollows
    else:
        account = AccountFollowers
        mode = "followers"

    account_list = account.objects.filter()
    
    sort_list = [
        # ID         アカウント名    今月          今日
        'id',        'account_name', 'month_now',  'today',
        # 1日前      2日前           3日前         4日前
        'prev_one',  'prev_two',     'prev_three', 'prev_four',
        # 5日前      6日前           7日前
        'prev_five', 'prev_six',     'prev_seven'
    ]

    if sort in sort_list:
        account_list = account_list.order_by(sort)    
    else:
        account_list = account_list.order_by('id')

    if order == 'desc':
        account_list = account_list.reverse()
    else:
        order = 'asc'

    context = {
        'mode'        : mode,
        'account_list': account_list,
        'sort'        : sort,
        'order'       : order
    }
    return render(request, 'dashboard/index.html', context)

@transaction.atomic
def add_account(request):
    
    account_name  = request.POST.get("account_name")

    if account_name == '':
        return JsonResponse({"code": 2001})

    count = AccountSummary.objects.filter(account_name = account_name).count()

    if 0 < count:
        return JsonResponse({"code": 2003})

    try:
        scrape.scrape_instagram(account_name)
    except JSONDecodeError:
        return HttpResponse(status=404)

    return JsonResponse({"code": 2002})
