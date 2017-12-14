# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=250)
    which_league = models.CharField(max_length=250)
    number_of_champions = models.CharField(max_length=250)
    logo = models.CharField(max_length=10000)
    def __str__(self):
        return "Team: " + self.team_name + " Leage: " + self.which_league + " Number Of Champions: " + self.number_of_champions

class Footballer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    def __str__(self):
        return "Footballer's Name: " + self.name + " Position: " + self.position
