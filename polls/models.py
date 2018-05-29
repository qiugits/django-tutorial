import datetime

from django.db import models as m
from django.utils import timezone


class Question(m.Model):
    question_text = m.CharField(max_length=200)
    pub_date = m.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(m.Model):
    question = m.ForeignKey(Question, on_delete=m.CASCADE)
    choice_text = m.CharField(max_length=200)
    votes = m.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
