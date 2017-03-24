from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests, json


def all_cars(request):
	r = requests.get('http://models-api:8000/api/v1/cars')
	j = JsonResponse(r.json())
	if j.status_code != 200:
		return JsonResponse({'ok': False, 'result': 'get request failed'})
	else:
		return j

def recently_added_cars(request):
  r = requests.get('http://models-api:8000/api/v1/cars')
  data = json.loads(r.text)
  dates = {};
  for car in data['result']:
    value = data['result'].get(car)
    dates.append({car: value['date_created']})
  dates.sort()
  return JsonResponse({'ok': True, 'result': dates[:2]})
