from django.db import models

class Airport(models.Model):
    code = models.CharField(("Airport Code "), max_length=3)
    city = models.CharField(("City Name"), max_length=50)

    def __str__(self):
        return f"{self.city} {self.code}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField(("duratin of flight in mintues"))
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}" 
    
class Passengers(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"