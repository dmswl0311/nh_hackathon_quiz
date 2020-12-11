from django.db import models


class Quiz(models.Model):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)


class OX_Quiz(models.Model):
    ox_question = models.TextField(blank=True)
    ox_answer = models.TextField(blank=True)
    ex_answer = models.TextField(blank=True)
