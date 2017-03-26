from django.http import JsonResponse
# from .models import User, Car, Buyers, Sellers
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import RegisterForm

# Create your views here.

def home_page(request):
	r = requests.get('http://exp-api:8000/exp/cars/recentlyadded')
	j = r.json()
	return render(request, 'web/homePage.html', {'cars': j})

def details(request):
	r = requests.get('http://exp-api:8000/exp/all/cars')
	j = r.json()
	return render(request, 'web/details.html', {'cars': j})

def register(request):
	registered = False

	if request.method == 'POST':
		register_form = RegisterForm(data=request.POST)

		if register_form.is_valid():
			user_id = register_form.cleaned_data['user_id']
			password = register_form.cleaned_data['password']
			r = request.post('http://exp-api:8000/exp/register', data={'user_id':user_id, 'password':password})
			return render(request, 'web/register.html', {'register_form': register_form})
		else:
			return JsonResponse(request, 'Username or password was not correctly entered', safe=False)

	else:
		register_form = RegisterForm()

	return render(request, 'web/register.html', {'register_form': register_form})
