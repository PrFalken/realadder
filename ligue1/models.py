from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    budget = models.FloatField()
    points = models.IntegerField()
    real_points = models.FloatField()
    def __unicode__(self):
        return self.name


