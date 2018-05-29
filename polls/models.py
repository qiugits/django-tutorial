import datetime

from django.db import models as m
from django.utils import timezone


class Question(m.Model):
    question_text = m.CharField(max_length=200)
    pub_date = m.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(m.Model):
    question = m.ForeignKey(Question, on_delete=m.CASCADE)
    choice_text = m.CharField(max_length=200)
    votes = m.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
