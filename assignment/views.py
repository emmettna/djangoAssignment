# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q

from assignment.models import User, User_team, User_resource, Match_list, Team_list, User_rank, Bet_list
from assignment.models import Player_table
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

    user_queryset = User.objects.get(usn=usn)
    user_team_queryset = User_team.objects.filter(usn=usn)
    user_resource_queryset = User_resource.objects.get(usn=usn)

    team_id_set = set()

    print(user_team_queryset)
    for e2 in user_team_queryset:

        # User_team object keeps team_id from team_list which makes the return value 'queryset'
        # So queryset turned to Dictionary to be added to Set
        # Set is not Json serializable so made it to list
        team_id_set.add(model_to_dict(e2.team_id).get('team_id'))

    object_Dictation = {'usn': user_queryset.usn,
                        'username': user_queryset.username,
                        'token': user_queryset.token,
                        'trophy': user_resource_queryset.trophy,
                        'team_id': list(team_id_set)}

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
    list_of_matches = []
    union_of_querysets = (Match_list.objects.
                          filter(Q(home_team_id__in=team_id_set) | Q(away_team_id__in=team_id_set)).
                          filter(match_date__range=(now, two_weeks)))

    def queryset_iterator(query_set):
        for element in query_set:
            match_time = element.match_time.isoformat()

            match_list_dictation = {
                'match_id': element.match_id,
                'home_team_id': element.home_team_id,
                'away_team_id': element.away_team_id,
                'match_date': element.match_date.isoformat(),
                'match_time': match_time[:5]
            }
            list_of_matches.append(match_list_dictation)

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

    # User Rank is Dummy ATM


def user_rank(request, usn):
    user_rank_queryset = User_rank.objects.get(usn=usn)

    # User Top 10 ranks Could be stored statically rather than calculating every time

    object_dictation_processed = {'user_rank': "Dummy Rank",
                                  'username': user_rank_queryset.usn.username,
                                  'user_rank_pt': user_rank_queryset.user_pt
                                  }
    json_object = json.dumps(object_dictation_processed)
    return HttpResponse(json_object, content_type="application/json")


def bet_list(request, usn):
    list_of_bets = []
    bet_list_queryset = Bet_list.objects.filter(usn=usn)
    for e in bet_list_queryset:
        bet_list_dict = {
                        'comp_id': e.comp_id.comp_id,
                        'match_id': e.match_id.match_id,
                        'A': e.bet_selected.win_draw_lose,
                        'B': e.bet_selected.scores,
                        'C': e.bet_selected.first_scorer.player_name
                        }
        list_of_bets.append(bet_list_dict)

    object_dictation_processed = {'usn': usn,
                                  'bet_list': list_of_bets}
    json_object = json.dumps(object_dictation_processed)
    return HttpResponse(json_object, content_type="application/json")


def bet_history(request, usn):
    bet_history_query = Bet_list.objects.filter(usn=usn)
    bet_history_dict = []
    for e in bet_history_query:
        bet_history_detail={'comp_id': e.comp_id.comp_id,
                            'match_id': e.match_id.match_id,
                            'match_date': e.match_id.match_date.isoformat(),
                            'match_time': e.match_id.match_time.isoformat(),
                            'home_team_id': e.match_id.home_team_id,
                            'away_team_id': e.match_id.away_team_id,
                            'scores': 'who actaully scored',
                            'first_scorer': 'who scored first',
                            'A':e.bet_selected.win_draw_lose,
                            'B':e.bet_selected.scores,
                            'C':e.bet_selected.first_scorer.player_name
                            }
        bet_history_dict.append(bet_history_detail)

        print(bet_history_dict)
    json_object = json.dumps(bet_history_dict)
    return HttpResponse(json_object, content_type="application/json")


def player_list(request, team_id):
    list_of_players = []
    player_list_query = Player_table.objects.filter(team_id=team_id)
    for e in player_list_query:
        player_dict = {'player_id': e.player_id,
                       'name': e.player_name,
                       'number': e.uni_num,
                       'position': e.position,
                       'appearance': 'dummy',
                       'goals': 'dummy',
                       'assists': 'dummy'
                       }
        list_of_players.append(player_dict)
    print(player_list_query)

    object_dictation_processed = {'version': datetime.now().isoformat()[:10],
                                  'team_id': team_id,
                                  'player_list': list_of_players}
    json_object = json.dumps(object_dictation_processed)
    return HttpResponse(json_object, content_type="application/json")