from unittest.util import _MAX_LENGTH
from django.db import models

class Chat1(models.Model):
    text1 = models.TextField(max_length=200)

    class Meta:
        db_table = 'chat1'

class Chat2(models.Model):
    text2 = models.TextField(max_length=200)

    class Meta:
        db_table = 'chat2'
