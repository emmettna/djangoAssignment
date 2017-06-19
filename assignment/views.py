# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource, Match_list, Team_list
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import loader
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.shortcuts import render


# Create your views here.

def user_profile(request, usn=1):

    # Take usn as a parameter then get user details which team the user likes
    # Then it searches both home and away team match
    # Finally wrap the details and return json object

    queryset = User.objects.filter(usn=usn)
    queryset2 = User_team.objects.filter(usn=usn)
    queryset3 = User_resource.objects.filter(usn=usn)

    team_Id = set()
    object_Dictation = ''

    for e in queryset:
        for e2 in queryset2:
            for e3 in queryset3:
                usn = e.usn
                username = e.username
                token = e.token
                trophy = e3.trophy

                # User_team object keeps team_id from team_list which makes the return value 'queryset'
                # So queryset turned to Dictionary to be added to Set
                # Set is not Json serializable so made it to list
                team_Id.add(model_to_dict(e2.team_id).get('team_id'))

                object_Dictation = {'usn': usn,
                        'username': username,
                        'token': token,
                        'trophy': trophy,
                        'team_id': list(team_Id)}

    JSon_Object = json.dumps(object_Dictation)

    return HttpResponse(JSon_Object, content_type="application/json")


def match_list(request, usn=1):

    queryset = User_team.objects.filter(usn=usn).values('team_id').distinct()
    # If you want to deal with Model object, you can replace 'values' with 'only'
    team_Id = []
    for e in queryset:
        team_Id.append(e.get('team_id'))

    # Match the team ids with match list. if it matches either home or away or both
    now = datetime.now()
    two_weeks = now + timedelta(days=14)
    print("now : ", now , "two weeks from now ", two_weeks)
    home_team_queryset = Match_list.objects.filter(home_team_id__in=team_Id).filter(match_date__range=(now, two_weeks))
    away_team_queryset = Match_list.objects.filter(away_team_id__in=team_Id).filter(match_date__range=(now, two_weeks))

    if not away_team_queryset:
        print("queryset is empty")
    # Needs to handle the case of the empty values(if none of matches are available)

    listOfMatch = []

    for e in home_team_queryset, away_team_queryset:
        match_id = e.match_id

        # Made the object dictated. I guess when it has multiple values, it can't be JSon serialized
        # For testing purpose, the function is loading all the function is loading just one value,
        # it may be fine.

        home_team_id = e.home_team.team_id
        # home team id is an object of teamlist. While it just needs to print team_id, it's printing entire row.
        away_team_id = e.away_team.team_id

        # Made the date object a String

        match_date = e.match_date.isoformat()
        match_time = e.match_time.isoformat()

        matchListDictation = {
            'match_id' : match_id,
            'home_team_id' : home_team_id,
            'away_team_id' : away_team_id,
            'match_date' : match_date,
            'match_time' : match_time
            }
        listOfMatch.append(matchListDictation)

    object_Dictation_Processed = {'usn' : usn,
                                  'match_list' : listOfMatch,
                                 }
    json_Object = json.dumps(object_Dictation_Processed)

    return HttpResponse(json_Object,content_type="application/json")
