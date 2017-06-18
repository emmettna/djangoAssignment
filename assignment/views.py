# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource, Match_list, Team_list
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.shortcuts import render


# Create your views here.

# Takes usn as parameter ~/user_profile/(usn)
# By usn number, function decides which user to retrieve from Database
# Through the for loops, values assigned to variables
# JSon object returned as requested


def user_profile(request, usn=1):

    #Version1 sending via user_profile.html

    # anotherqueryset = User.objects.filter(usn=usn
    # anotherqueryset2 = User_team.objects.filter(usn=usn)
    # anotherqueryset3 = User_resource.objects.filter(usn=usn)
    #
    # list = []
    # list.append(anotherqueryset2)
    # for e in anotherqueryset2:
    #     list.append(e.team_id)
    # print(list)
    #
    # context = {
    #     'User' : anotherqueryset,
    #     'User_team' : list,
    #     'User_resource' : anotherqueryset3
    # }
    # return render(request,'user_profile.html',context)

    # Version2 sending JSon file directly

    queryset = User.objects.filter(usn=usn)
    queryset2 = User_team.objects.filter(usn=usn)
    queryset3 = User_resource.objects.filter(usn=usn)

    usn = ''
    username = ''
    token = ''
    trophy = ''
    team_Id = []

    for e in queryset:
        for e2 in queryset2:
            for e3 in queryset3:
                usn = e.usn
                username = e.username
                token= e.token
                trophy = e3.trophy
                team_Id.append(e2.team_id)

    object_Dictation = {'usn': usn,
                        'username': username,
                        'token': token,
                        'trophy': trophy,
                        'team_id': team_Id}

    JSon_Object = json.dumps(object_Dictation)

    return HttpResponse(JSon_Object, content_type="application/json")

    # Take usn as a parameter then get user details which team the user likes
    # Then it searches both home and away team match
    # Finally wrap the details and return json object

def match_list(request, usn=1):

    queryset = User_team.objects.filter(usn=usn).values('team_id').distinct()

    team_Id = []
    for e in queryset:
        team_Id.append(e)

    # Get data from user_team and put it in team_id list
    # for e in queryset:
    #      team_Id.append(e.team_id)

    print(team_Id)

    # Match the team ids with match list. if it matches either home or away or both
    # Then it returns.
    # Issue #1 user_team model has three rows [id, team_id_id, usn_id] and when it filters,
    # it filters by id not by team_id_id.

    queryset4 = Match_list.objects.get(home_team_id=5)
    queryset3 = Match_list.objects.all()
    print('home team' , queryset4)

    match_id = ''
    home_team_id = ''
    away_team_id = ''
    match_date = ''
    match_time = ''

    for e in queryset3:
        match_id = e.match_id
        print(match_id)

        # Made the object dictated. I guess when it has multiple values, it can't be JSon serialized
        # For testing purpose, the function is loading all the function is loading just one value,
        # it may be fine.

        home_team_id = model_to_dict(e.home_team.team_id).get('team_id','')
        print(home_team_id)
        # home team id is an object of teamlist. While it just needs to print team_id, it's printing entire row.
        away_team_id = model_to_dict(e.away_team.team_id).get('team_id','')

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
    print(matchListDictation)

    object_Dictation_Processed = {'usn' : usn,
                                  'match_list' : matchListDictation
                                 }
    JSon_Object = json.dumps(object_Dictation_Processed)

    return HttpResponse(JSon_Object,content_type="application/json")
