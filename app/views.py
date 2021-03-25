from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from app.models import Bin, Operation, BinOperation
from datetime import datetime, timedelta
from django.template import Context, loader
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Bin-Operation App")


def collection_frequency(request):
    data = BinOperation.objects.all()

    results = []
    for item in data:
        result = {'bin': item.bin.id, 'operation' : item.operation.name,
         'collection_frequency' : item.collection_frequency}
        results.append(result)
   
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')
