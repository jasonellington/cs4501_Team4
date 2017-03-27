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
  r = requests.get('http://models-api:8000/api/v1/cars/recentlyadded')
  j = r.json()
  cars = {}
  ids = [item[0] for item in j['result']]
  for car_id in ids:
    temp = requests.get('http://models-api:8000/api/v1/car/%d' % int(car_id))
    cars[car_id] = temp.json()['result']
  return JsonResponse(cars)

def register(request):
  if request.method == 'POST':
      r = requests.post('http://models-api:8000/api/v1/create/user', request.POST)
      return HttpResponse(r.text)

  return HttpResponse(request.method)

def create_listing(request):
  if request.method == 'POST':
    r = requests.post('http://models-api:8000/api/v1/create/car', request.POST)
    return HttpResponse(r.text)

  return HttpResponse(request.method)

def login_add_authenticator(request):

  if request.method == 'POST':

    if request.POST.get('user_id'):
         user_id = request.POST.get('user_id')
    
    if request.POST.get('password'):
         password = request.POST.get('password')

    temp = requests.get('http://models-api:8000/api/v1/user/%s' % user_id)
    return HttpResponse(temp)
    temp_pass = 'blah'
    temp_pass = temp.json()['password']

    if password == temp_pass:

      r = requests.post('http://models-api:8000/api/v1/add_auth', request.POST)
      return HttpResponse(r.text)

  return HttpResponse(request.method)



