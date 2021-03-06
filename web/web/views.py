from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from elasticsearch import Elasticsearch
import requests, json
from .forms import RegisterForm, NewListingForm, LoginForm, SearchForm

def home_page(request):
    r = requests.get('http://exp-api:8000/exp/cars/recentlyadded')
    j = r.json()
    return render(request, 'web/homePage.html', {'cars': j})


def details(request):
    form = SearchForm
    r = requests.get('http://exp-api:8000/exp/all/cars')
    j = r.json()
    return render(request, 'web/details.html', {'cars': j, 'form': form})


def logged_in(request):
    form = SearchForm
    r = requests.get('http://exp-api:8000/exp/all/cars')
    j = r.json()
    return render(request, 'web/logged_in.html', {'cars': j, 'form': form})


def register(request):
    args = {}
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
            if r.json()['ok'] is True:
                return render(request, 'web/confirm_register.html', {'post_data': post_data})
            else:
                return render(request, 'web/register.html', {'form': RegisterForm(), 'error': 'Username already in use.'})
        else:
            register_form = RegisterForm()
            args['form'] = form
            return render(request, 'web/register.html', args)

    return render(request, 'web/register.html', {'form': RegisterForm()})

def login(request):
    r = requests.get('http://exp-api:8000/exp/all/cars')
    j = r.json()
    #check to see if the authenticator saved in cookies is the authenticator
    if request.COOKIES.get('my_user_authenticator') is not None:
        form = SearchForm
        post_data = {'authenticator': request.COOKIES.get('my_user_authenticator')}
        return render(request, 'web/logged_in.html', {'cars': j, 'form':form})

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'web/login.html', {'form': LoginForm, 'cars': j})

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            post_data = {
                'user_id': form.cleaned_data['user_id'],
                'password': form.cleaned_data['password']
            }

            r = requests.post('http://exp-api:8000/exp/login', post_data)
            if r.json()['ok'] is True:
                form = SearchForm
                authenticator = r.json()['result']['authenticator']
                response = render(request, 'web/logged_in.html', {'cars': j, 'form':form})
                response.set_cookie('my_user_authenticator', authenticator)
                return response
            else:
                return render(request, 'web/login.html', {'form': LoginForm, 'error': 'Invalid username or password'})

def create_listing(request):
    args = {}

    if request.COOKIES.get('my_user_authenticator') is not None:
        post_data = {'authenticator': request.COOKIES.get('my_user_authenticator')}
        r = requests.post('http://exp-api:8000/exp/check_auth', post_data)

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
                if r.json()['ok'] is True:
                    return render(request, 'web/listing_created.html', {'post_data': post_data, 'kafka-test': r.json()['result']})
                else:
                    return render(request, 'web/create_listing.html', {'form': NewListingForm(), 'error': 'Duplicate Listing'})
            else:
                create_form = NewListingForm()
                args['form'] = form
                return render(request, 'web/create_listing.html', args)
        else:
            return render(request, 'web/create_listing.html', {'form': NewListingForm()})

    else:
        return HttpResponse('Not logged in.')

def log_out(request):
    #if the cookie doesn't exist then do not send the request

    if request.method == 'GET':
        if request.COOKIES.get('my_user_authenticator') is not None:
            post_data = {'authenticator': request.COOKIES.get('my_user_authenticator')}
            r = requests.post('http://exp-api:8000/exp/log_out', post_data)
            if r.json()['ok'] is True:
                r = requests.get('http://exp-api:8000/exp/cars/recentlyadded')
                j = r.json()
                response = render(request, 'web/homePage.html', {'cars': j})
                response.delete_cookie('my_user_authenticator')
                return response
            else:
                return HttpResponse("Logout failed. Please try again.")
        else:
            r = requests.get('http://exp-api:8000/exp/cars/recentlyadded')
            j = r.json()
            return render(request, 'web/homePage.html', {'cars': j})
    else:
        return HttpResponse("Must be a GET request")


# @login_required
def cookie(request):
    return render(request, 'web/cookie.html')


# @login_required
def search_results(request):
    return render(request, 'web/search_results.html')

# @login_required
def search(request):
    user = False
    if request.COOKIES.get('my_user_authenticator') is not None:
        user = True

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            post_data = {'query': form.cleaned_data['query']}

            r = requests.post('http://exp-api:8000/exp/search', post_data)
            j = r.json()

            return render(request, 'web/search_results.html', {'search_results': j['result'], 'user': user})
    else:
        form = SearchForm
        r = requests.get('http://exp-api:8000/exp/all/cars')
        j = r.json()
        return render(request, 'web/search.html', {'cars': j, 'form': form, 'user': user})


def single_listing_result(request):
     return render(requerst, 'web/single_listing_result.html')


def single_listing(request, id):
    logged_in = False
    if request.COOKIES.get('my_user_authenticator') is not None:
        logged_in = True

    if request.method == 'GET':
            post_data = {'car_id': id, 'authenticator': request.COOKIES.get('my_user_authenticator')}

            r = requests.post('http://exp-api:8000/exp/cars/single_car', post_data)
            j = r.json()

            return render(request, 'web/single_listing_result.html', {'single_listing_result': j['result'], 'logged_in': logged_in})
    else:
        r = requests.get('http://exp-api:8000/exp/all/cars')
        j = r.json()
        return render(request, 'web/logged_in.html', {'cars': j, 'user': user})






