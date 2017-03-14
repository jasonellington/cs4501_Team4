from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests


def all_cars(request):
	r = requests.get('http://models-api:8000/api/v1/cars')
	if r.raise_for_status() != 200:
		return JsonResponse({'ok': False, 'result': 'get request failed'})
	else:
		return r.json()
