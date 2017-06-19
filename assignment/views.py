# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource, Match_list, Team_list
from django.http import HttpResponse
from datetime import datetime, timedelta
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
    team_id_queryset = User_team.objects.filter(usn=usn).values('team_id').distinct()
    # It takes Usn and returns team_id objects
    # If you want to deal with Model object, you can replace 'values' with 'only'
    team_id_set = set()
    for e in team_id_queryset:
        team_id_set.add(e.get('team_id'))

    now = datetime.now()
    two_weeks = now + timedelta(days=14)

    # There may be a way to loading both Home and Away team id at the same time.

    home_team_queryset = Match_list.objects.filter(home_team_id__in=team_id_set).filter(match_date__range=(now, two_weeks))
    away_team_queryset = Match_list.objects.filter(away_team_id__in=team_id_set).filter(match_date__range=(now, two_weeks))

    # Needs to handle the case of the duplicate

    list_of_matches = []
    union_of_querysets = home_team_queryset.union(away_team_queryset)

    def queryset_iterator(query_set):
        for element in query_set:
            match_id = element.match_id
            home_team_id = element.home_team.team_id
            away_team_id = element.away_team.team_id

            # Made the date object a String

            match_date = element.match_date.isoformat()
            match_time = element.match_time.isoformat()

            matchListDictation = {
                'match_id': match_id,
                'home_team_id': home_team_id,
                'away_team_id': away_team_id,
                'match_date': match_date,
                'match_time': match_time
            }
            list_of_matches.append(matchListDictation)

    if not union_of_querysets.exists():
        # Handle the empty case here.
        print('QuerySets are empty, You need to add values other wise it will return a blank dictionary object')
    else:
        queryset_iterator(union_of_querysets)

    object_dictation_processed = {'usn': int(usn),
                                  'match_list': list_of_matches,
                                  }
    json_object = json.dumps(object_dictation_processed)

    return HttpResponse(json_object, content_type="application/json")
