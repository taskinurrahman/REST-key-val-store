from django.shortcuts import render
from key_value.models import Store
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,timedelta
from django.core import serializers

# Create your views here.
@csrf_exempt
def values(request):
    
    if request.method == "GET":

        Store.objects.filter(created_at__lte = (datetime.now() - timedelta(minutes = 5))).delete()
        # return key values
        keys = request.GET.get('keys', None)
        if keys is None:
            # return all value
            data = {}
            store = Store.objects.all()
            for row  in store:
                data[row.key] = row.value
                
            return JsonResponse(data)
        else:
            store = Store.objects.all()
            allKeys = keys.split(',')
            data = {}
            for row  in store:
                if(row.key in allKeys):
                    temp_store = Store.objects.filter(key = row.key).get()
                    temp_store.created_at = datetime.now()
                    temp_store.save()
                    data[row.key] = temp_store.value
            return JsonResponse(data)

    if request.method == "POST":
        #save data
        data = json.loads(request.body)
        for k in data:
            store = Store(key=k, value=data[k],created_at = datetime.now())
            store.save()
        return JsonResponse({})
        
    if request.method == "PATCH":
        # edits data
        store = Store.objects.all()
        data = json.loads(request.body)
        for row  in store:
            if(row.key in data.keys()):
                temp_store = Store.objects.filter(key = row.key).get()
                temp_store.created_at = datetime.now()
                temp_store.value = data[row.key]
                temp_store.save()
    return JsonResponse({})