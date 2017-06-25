# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0011_auto_20170619_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_num', models.IntegerField(unique=True)),
                ('user_pt', models.IntegerField()),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User')),
            ],
        ),
        migrations.AlterField(
            model_name='match_list',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='assignment.Team_list'),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='assignment.Team_list'),
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
    ]
