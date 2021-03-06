# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0012_auto_20170622_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bet_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bet_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_draw_lose', models.CharField(max_length=1)),
                ('scores', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Comp_table',
            fields=[
                ('comp_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('comp_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Player_table',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('player_name', models.CharField(max_length=50)),
                ('uni_num', models.IntegerField()),
                ('position', models.CharField(max_length=10)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Team_list')),
            ],
        ),
        migrations.AlterField(
            model_name='user_rank',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User'),
        ),
        migrations.AlterField(
            model_name='user_resource',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User'),
        ),
        migrations.AlterField(
            model_name='user_team',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User'),
        ),
        migrations.AddField(
            model_name='bet_table',
            name='first_scorer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Player_table'),
        ),
        migrations.AddField(
            model_name='bet_list',
            name='bet_selected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Bet_table'),
        ),
        migrations.AddField(
            model_name='bet_list',
            name='comp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Comp_table'),
        ),
        migrations.AddField(
            model_name='bet_list',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Match_list'),
        ),
        migrations.AddField(
            model_name='bet_list',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User'),
        ),
        migrations.AddField(
            model_name='bet_history',
            name='bet_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Bet_table'),
        ),
        migrations.AddField(
            model_name='bet_history',
            name='comp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Comp_table'),
        ),
        migrations.AddField(
            model_name='bet_history',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Match_list'),
        ),
    ]
