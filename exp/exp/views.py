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

def register(request):
	params = {'user_id':'user_id', 'password':'password'}
	r = request.POST('http://models-api:8000/api/v1/create/user', data=params)
	j = JsonResponse(r.json())
	if j.status_code != 200:
		return JsonResponse({'ok': False, 'result': 'get request failed'})
	else:
		return j

def listing_created(request):
	params = {'make':'make', 'car_model':{{ model }}, 'year':'year', 'color':'color', 'body_type':'body_type', 'num_seats':'num_seats'}
	r = requests.post('http://models-api:8000/api/v1/create/car', data=params)
	return r.json();