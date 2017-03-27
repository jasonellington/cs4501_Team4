from django.http import JsonResponse
# from .models import User, Car, Buyers, Sellers
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import RegisterForm, NewListingForm, LoginForm

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
  if request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      post_data = {
            'user_id': form.cleaned_data['user_id'],
            'password': form.cleaned_data['password'],
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'age': form.cleaned_data['age'],
            'rating': 0
      }
      r = requests.post('http://exp-api:8000/exp/register', post_data)
      return render(request, 'web/confirm_register.html', {'post_data': post_data})
			
    else:
      register_form = RegisterForm()

  return render(request, 'web/register.html', {'form': RegisterForm()})

def login(request):
	form_class = LoginForm

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			post_data = {
            'user_id': form.cleaned_data['user_id'],
            'password': form.cleaned_data['password'],
      }
			#r = requests.post('http://exp-api:8000/exp/create/listing', post_data)
			return render(request, 'web/logged_in.html', {'post_data': post_data})

		else:
			form = LoginForm()

	return render(request, 'web/login.html', {'form': form_class})

def logged_in(request):

	return render(request, 'web/logged_in.html')

def create_listing(request):
	form_class = NewListingForm

	if request.method == 'POST':
		form = NewListingForm(request.POST)

		if form.is_valid():
			post_data = {
            'make': form.cleaned_data['make'],
            'model': form.cleaned_data['model'],
            'year': form.cleaned_data['year'],
            'color': form.cleaned_data['color'],
            'body_type': form.cleaned_data['body_type'],
            'num_seats': form.cleaned_data['num_seats']
      }
			r = requests.post('http://exp-api:8000/exp/create/listing', post_data)
			return render(request, 'web/listing_created.html', {'post_data': post_data})

		else:
			form = NewListingForm()

	return render(request, 'web/create_listing.html', {'form': form_class})
