# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is sport home page</h1>')

def football(request,team_name):
    return HttpResponse('<h1>I would like to play football at %s</h1>' %(str(team_name)))