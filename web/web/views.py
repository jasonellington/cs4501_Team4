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
	
	#check to see if the authenticator saved in cookies is the authenticator
	if request.COOKIES.get('my_user_authenticator') != None:
		post_data = {'authenticator': request.COOKIES.get('my_user_authenticator')}
		return render(request, 'web/cookie.html')

	if request.method == 'GET':
		form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			post_data = {
            'user_id': form.cleaned_data['user_id'],
            'password': form.cleaned_data['password'],
      		}

			r = requests.post('http://exp-api:8000/exp/login', post_data)
			if r.json()['ok'] == True:
				authenticator = r.json()['result']['authenticator']
				response = render(request, 'web/logged_in.html')
				response.set_cookie('my_user_authenticator', authenticator)
				return response


	return render(request, 'web/login.html', {'form': form_class})

def create_listing(request):
	form_class = NewListingForm

	if request.COOKIES.get('my_user_authenticator') != None:
		post_data = {'authenticator': request.COOKIES.get('my_user_authenticator')}
		return HttpResponse('You must be logged in the view this page!')

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


def log_out(request):
	if request.method == 'GET':
		post_data = {'authenticator': request.COOKIES.get('my_user_authenticator')}
		r = requests.post('http://exp-api:8000/exp/log_out', post_data)
		if r.status_code == 200:
			response = render(request, 'web/homePage.html')
			response.delete_cookie('my_user_authenticator')
			form = LoginForm()
			return response
		else:
			return HttpResponse("Authenticator not found")
	else:
		return HttpResponse("Must be a GET request")

def logged_in(request):

	return render(request, 'web/logged_in.html')

# @login_required
def cookie(request):

	return render(request, 'web/cookie.html')