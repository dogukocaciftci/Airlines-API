from django.db import models

# Create your models here.


class Airline(models.Model):
    name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=20)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Aircraft(models.Model):
    manufacturer_serial_number = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    operator_airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    number_of_engines = models.IntegerField()

    def __str__(self):
        return self.model
