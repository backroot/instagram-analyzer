from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=100)
    password     = models.CharField(max_length=255)
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

class AccountSummary(models.Model):
    user_id      = models.IntegerField()
    account_name = models.CharField(max_length=100)
    scrape_date  = models.DateField()
    posts        = models.IntegerField()
    followers    = models.IntegerField()
    follows      = models.IntegerField()
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

    class Meta:
            unique_together = [['user_id', 'account_name', 'scrape_date']]
            indexes = [
                models.Index(fields=['posts']),
                models.Index(fields=['followers']),
                models.Index(fields=['follows'])
            ]
