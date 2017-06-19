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
        return str(self.usn)

    def __int__(self):
        return self.username


class User_resource(models.Model):
    usn = models.ForeignKey('assignment.User', on_delete=models.CASCADE)

    trophy = models.IntegerField()

    def __str__(self):
        return str(self.usn)

    def __int__(self):
        return self.usn


class User_team(models.Model):
    usn = models.ForeignKey('assignment.User', on_delete=models.CASCADE, db_index=True)

    team_id = models.ForeignKey('assignment.Team_List')

    def __str__(self):
        return str(self.team_id.team_id)

    def __int__(self):
        return self.usn

class Team_list(models.Model):
    team_id = models.IntegerField(primary_key=True, unique=True)

    team_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.team_id)

# need to check where the hell Team_list is located then fix the bug

class Match_list(models.Model):
    match_id = models.IntegerField(primary_key=True)

    home_team = models.ForeignKey(Team_list,
                                  related_name='home')

    away_team = models.ForeignKey(Team_list,
                                  related_name='away')

    match_date = models.DateField()

    match_time = models.TimeField()

    def __str__(self):
        return str(self.match_id)
