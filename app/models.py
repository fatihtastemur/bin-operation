from django.db import models
from django.utils import timezone

class Operation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)


class Bin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    latitude = models.FloatField()
    longtitude = models.FloatField()


class BinOperation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField(auto_now_add=True, blank=True)

   
