import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Max
from django.contrib.auth.models import User

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

    @property
    def choice_count(self):
        return self.choice_set.all().count()

    @property
    def vote_count(self):
        count = 0
        for choice in self.choice_set.all():
            count += choice.votes
        return count

    @property
    def max_choice_count(self):
        question_choices = self.choice_set.all().order_by('votes').first()
        if question_choices == None:
            return 'N/A - no answers'
        elif question_choices.votes == 0:
            return 'N/A - no votes'
        else:
            return question_choices.choice_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Department(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=1000)
    head = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    email = models.EmailField()
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
