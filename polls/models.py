import datetime

from django.db import models
from django.utils import timezone

def create_question(question_text, days=0):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


def create_choices(choice_map, question):
    """
    Create a map of choices and votes with the given `choice_map` and the
    given question of `question_pk`.
    """
    # print(choice_map.items())
    choices = []
    for choice, votes in choice_map.items():
        choices.append(Choice.objects.create(
            choice_text=choice,
            votes=votes,
            question=question
        ))
    return choices


def create_poll(question_text, choice_map, days=0):
    question = create_question(question_text=question_text, days=days)
    choices = create_choices(choice_map, question)
    return [question, choices]

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        
