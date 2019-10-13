from django.db import models

class user(models.Model):
    name         = models.CharField(max_length=100)
    password     = models.CharField(max_length=255)
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

class account(models.Model):
    user_id      = models.IntegerField()
    account_name = models.CharField(max_length=100)
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

class follower(models.Model):
    account_id  = models.IntegerField()
    scrape_date = models.DateField()
    followers   = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class follow(models.Model):
    account_id  = models.IntegerField()
    scrape_date = models.DateField()
    follows     = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
