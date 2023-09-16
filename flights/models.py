from django.db import models

class Flight(models.Model):
    origin = models.CharField(("origin of the flight"), max_length=50)
    destination = models.CharField(("destination of the flight"), max_length=50)
    duration = models.IntegerField(("duratin of flight in mintues"))