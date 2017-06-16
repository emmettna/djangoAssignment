# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from datetime import datetime
import json


# Create your models here.

class User(models.Model):
    usn = models.IntegerField(primary_key=True, unique=True)

    username = models.CharField(max_length=20)

    token = models.CharField(max_length=8)

    def __str__(self):
        return self.username


class User_resource(models.Model):
    usn = models.ForeignKey('assignment.User', on_delete=models.CASCADE)

    trophy = models.IntegerField()

    def __int__(self):
        return self.trophy


class User_team(models.Model):
    usn = models.ForeignKey('assignment.User', on_delete=models.CASCADE)

    team_id = models.IntegerField()

    def __int__(self):
        return self.team_id


class Match_list(models.Model):
    match_id = models.IntegerField()

    home_team = models.ForeignKey(User_team,related_name='home')

    away_team = models.ForeignKey(User_team, related_name='away')

    match_date = models.DateField()

    match_time = models.TimeField()
