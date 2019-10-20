from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=100)
    password     = models.CharField(max_length=255)
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

class AccountSummary(models.Model):
    account_name    = models.CharField(max_length=100)
    profile_pic_url = models.CharField(max_length=512, default='') 
    scrape_date     = models.DateField()
    posts           = models.IntegerField(default=0)
    followers       = models.IntegerField(default=0)
    follows         = models.IntegerField(default=0)
    create_date     = models.DateTimeField(auto_now_add=True)
    update_date     = models.DateTimeField(auto_now=True)

    class Meta:
            unique_together = [['account_name', 'scrape_date']]
            indexes = [
                models.Index(fields=['posts']),
                models.Index(fields=['followers']),
                models.Index(fields=['follows'])
            ]

class AccountFollowers(models.Model):
    account_name    = models.CharField(max_length=100)
    profile_pic_url = models.CharField(max_length=512, default='') 
    month_now       = models.IntegerField(blank=True, null=True)
    month_prev      = models.IntegerField(blank=True, null=True)
    month_diff      = models.IntegerField(blank=True, null=True)
    today           = models.IntegerField(blank=True, null=True)
    today_diff      = models.IntegerField(blank=True, null=True)
    prev_one        = models.IntegerField(blank=True, null=True)
    prev_one_diff   = models.IntegerField(blank=True, null=True)
    prev_two        = models.IntegerField(blank=True, null=True)
    prev_two_diff   = models.IntegerField(blank=True, null=True)
    prev_three      = models.IntegerField(blank=True, null=True)
    prev_three_diff = models.IntegerField(blank=True, null=True)
    prev_four       = models.IntegerField(blank=True, null=True)
    prev_four_diff  = models.IntegerField(blank=True, null=True)
    prev_five       = models.IntegerField(blank=True, null=True)
    prev_five_diff  = models.IntegerField(blank=True, null=True)
    prev_six        = models.IntegerField(blank=True, null=True)
    prev_six_diff   = models.IntegerField(blank=True, null=True)
    prev_seven      = models.IntegerField(blank=True, null=True)
    prev_seven_diff = models.IntegerField(blank=True, null=True)
    prev_eight      = models.IntegerField(blank=True, null=True)
    create_date     = models.DateTimeField(auto_now_add=True)
    update_date     = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['account_name']),
            models.Index(fields=['month_now']),
            models.Index(fields=['today']),
            models.Index(fields=['prev_one']),
            models.Index(fields=['prev_two']),
            models.Index(fields=['prev_three']),
            models.Index(fields=['prev_four']),
            models.Index(fields=['prev_five']),
            models.Index(fields=['prev_six']),
            models.Index(fields=['prev_seven']),
        ]

class AccountFollows(models.Model):
    account_name    = models.CharField(max_length=100)
    profile_pic_url = models.CharField(max_length=512, default='') 
    month_now       = models.IntegerField(blank=True, null=True)
    month_prev      = models.IntegerField(blank=True, null=True)
    month_diff      = models.IntegerField(blank=True, null=True)
    today           = models.IntegerField(blank=True, null=True)
    today_diff      = models.IntegerField(blank=True, null=True)
    prev_one        = models.IntegerField(blank=True, null=True)
    prev_one_diff   = models.IntegerField(blank=True, null=True)
    prev_two        = models.IntegerField(blank=True, null=True)
    prev_two_diff   = models.IntegerField(blank=True, null=True)
    prev_three      = models.IntegerField(blank=True, null=True)
    prev_three_diff = models.IntegerField(blank=True, null=True)
    prev_four       = models.IntegerField(blank=True, null=True)
    prev_four_diff  = models.IntegerField(blank=True, null=True)
    prev_five       = models.IntegerField(blank=True, null=True)
    prev_five_diff  = models.IntegerField(blank=True, null=True)
    prev_six        = models.IntegerField(blank=True, null=True)
    prev_six_diff   = models.IntegerField(blank=True, null=True)
    prev_seven      = models.IntegerField(blank=True, null=True)
    prev_seven_diff = models.IntegerField(blank=True, null=True)
    prev_eight      = models.IntegerField(blank=True, null=True)
    create_date     = models.DateTimeField(auto_now_add=True)
    update_date     = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['account_name']),
            models.Index(fields=['month_now']),
            models.Index(fields=['today']),
            models.Index(fields=['prev_one']),
            models.Index(fields=['prev_two']),
            models.Index(fields=['prev_three']),
            models.Index(fields=['prev_four']),
            models.Index(fields=['prev_five']),
            models.Index(fields=['prev_six']),
            models.Index(fields=['prev_seven']),
        ]

