from django.db import models

class TeamScore(models.Model):
    team_score = models.IntegerField(default=0)

class TeamPositionDictionary(models.Model):
    name = models.IntegerField(default=0)

class TeamPosition(models.Model):
    teamPositionDictionary = models.ForeignKey(TeamPositionDictionary, on_delete=models.CASCADE, related_name="team_positions")
    key = models.IntegerField(default=0)
    value = models.IntegerField(default=0)




class Map(models.Model):
    name = models.IntegerField(default=0)

class MapKey(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="map_keys")
    key = models.IntegerField(default=0)

class MapValues(models.Model):
    mapKey = models.ForeignKey(MapKey, on_delete=models.CASCADE, related_name="map_values")
    key = models.CharField(max_length=1)
    value = models.IntegerField(default=501)

