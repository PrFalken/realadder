#!/usr/bin/python

from ligue1.models import Club
import urllib2
from lxml import etree

RANKINGS_URL = "http://query.yahooapis.com/v1/public/yql?q=use%20%22https%3A%2F%2Fraw.github.com%2Fymainier%2Fsoccer_tables%2Fmaster%2Franking.xml%22%20as%20ranking%3B%20select%20*%20from%20ranking%20where%20league%3D%22french%22%3B&diagnostics=true"

rawxml = urllib2.urlopen(RANKINGS_URL).read()
root = etree.fromstring(rawxml)

# Get Ligue 1 Teams and points
team_points  = {}
for team in root.find("results").find("ranking"):
    team_name = team.find("name").text
    team_points[team_name] = team.find('points').text

# Feed the database
for clubname in team_points:
    try:
        c = Club.objects.get(name=clubname)
        c.points = team_points[clubname]
    except Club.DoesNotExist:
        c = Club(name=clubname,  points=team_points[clubname], budget=0)
    if c.budget != 0:
        c.real_points = float(c.points) / float(c.budget) 
    else:
        c.real_points = 0
    c.save()

# Clean wrong clubs
for c in Club.objects.all():
    if c.name not in team_points.keys():
        c.delete()
        
