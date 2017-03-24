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
	r = request.post({user_id: request.post['user_id'], passsword: request.post['password'], 'http://models-api:8000/api/v1/create/user')
	j = JsonResponse(r.json())
	if j.status_code != 200:
		return JsonResponse({'ok': False, 'result': 'get request failed'})
	else:
		return j
