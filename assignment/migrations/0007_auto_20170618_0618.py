# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_auto_20170618_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_list',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team_list',
            name='id',
        ),
        migrations.AlterField(
            model_name='match_list',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='assignment.User_team'),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='assignment.User_team'),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='match_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='team_list',
            name='team_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_resource',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='assignment.User'),
        ),
        migrations.AlterField(
            model_name='user_team',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User'),
        ),
    ]
