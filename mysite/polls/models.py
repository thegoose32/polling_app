import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def vote_count(self):
        count = 0
        for choice in self.choice_set.all:
            count += choice.votes
        return count

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_size = models.IntegerField(default=0)
    company_start_year = models.IntegerField(max_length=4)
    def __str__(self):
        return self.company_name

class User(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_role = models.CharField(max_length=50)
