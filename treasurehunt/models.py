from django.db import models

class TeamData(models.Model):
    # Storing the map as a string that we will then convert to dictionary object
    map = models.CharField(max_length=100000)
    # Storing team position as a string that we will then convert to dictionary object
    team_position = models.CharField(max_length=10000)
    team_score = models.IntegerField(default=0)

