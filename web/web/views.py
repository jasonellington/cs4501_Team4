from django.http import JsonResponse
# from .models import User, Car, Buyers, Sellers
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import RegisterForm, NewListingForm

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
		register_form = RegisterForm(request.POST)

		if register_form.is_valid():
			user_id = register_form.cleaned_data['user_id']
			password = register_form.cleaned_data['password']
		else:
			register_form = RegisterForm()

	return render(request, 'web/register.html', {'form': register_form, 'user_id': user_id, 'password':password})

def login(request):
	
	return render(request, 'web/login.html')

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
			return JsonResponse(r.raise_for_status())
			# return HttpResponseRedirect('web/listing_created.html')

		else:
			form = NewListingForm()

	return render(request, 'web/create_listing.html', {'form': form_class})

def listing_created(request):
	if request.method == 'POST':

		form = NewListingForm(request.POST)

		if form.is_valid():
			make = form.cleaned_data['make']
			model = form.cleaned_data['model']
			year = form.cleaned_data['year']
			color = form.cleaned_data['color']
			body_type = form.cleaned_data['body_type']
			num_seats = form.cleaned_data['num_seats']
		else:
			form = NewListingForm()

	return render(request, 'web/listing_created.html', {'request': request.POST, 'form': NewListingForm, 'make':make, 'model':model, 'year':year, 'color':color, 'body_type':body_type, 'num_seats':num_seats})

