from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import hashers
from kafka import KafkaProducer
from elasticsearch import Elasticsearch
import requests
import json


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


def single_car(request):
    if request.method == 'POST':
        auth = request.POST.get('authenticator')
        r = requests.get('http://models-api:8000/api/v1/auth/%s' % request.POST.get('authenticator'))
        j = r.json()

        producer = KafkaProducer(bootstrap_servers='kafka:9092')

        item_viewed = {
            'user_id': j['user_id'],
            'car_id': request.POST.get('car_id')
        }

        user_id = j['user_id']

        producer.send('popular-items', json.dumps(item_viewed).encode('utf-8'))

        r = requests.get('http://models-api:8000/api/v1/car/%d' % int(request.POST.get('car_id')))
        j = r.json()
        return JsonResponse(j)

    return JsonResponse({'ok': False, 'result': 'Not a post'})


def register(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/api/v1/create/user', request.POST)
        return JsonResponse(r.json())

    return JsonResponse({'ok': False, 'result': 'Not a post'})


def create_listing(request):
    if request.method == 'POST':

        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')
        color = request.POST.get('color')
        body_type = request.POST.get('body_type')
        num_seats = request.POST.get('num_seats')

        r = requests.post('http://models-api:8000/api/v1/create/car', request.POST)
        j = r.json()

        producer = KafkaProducer(bootstrap_servers='kafka:9092')

        new_listing = {
            'id': j['result']['id'],
            'make': j['result']['make'],
            'car_model': j['result']['car_model'],
            'year': j['result']['year'],
            'color': j['result']['color'],
            'body_type': j['result']['body_type'],
            'num_seats': j['result']['num_seats'],
            'date_created': j['result']['date_created']
        }

        producer.send('new-listings-topic', json.dumps(new_listing).encode('utf-8'))

        return JsonResponse({'ok': True, 'result': new_listing})

    return HttpResponse(request.method)


def check_auth(request):
    if request.method == 'POST':
        if request.POST.get('authenticator'):

            authenticator = request.POST.get('authenticator')
            a = requests.get('http://models-api:8000/api/v1/check_auth/%s' % authenticator)
            compare_authenticator = a.json()['authenticator']

            if authenticator == compare_authenticator:
                return JsonResponse(compare_authenticator)


def login_add_authenticator(request):
    if request.method == 'POST':
        if request.POST.get('user_id'):
                user_id = request.POST.get('user_id')
                u = requests.get('http://models-api:8000/api/v1/userid/%s' % user_id)

                if u.json()['ok'] is True:
                    if request.POST.get('password'):
                        password = request.POST.get('password')
                        p = requests.get('http://models-api:8000/api/v1/password/%s' % user_id)

                        if p.json()['ok'] is True:
                            compare_password = p.json()['password']
                            if hashers.check_password(password, compare_password):
                                r = requests.post('http://models-api:8000/api/v1/add_auth', request.POST)
                                if r.json()['ok'] is True:
                                    return JsonResponse(r.json())

    return JsonResponse({'ok': False, 'result': 'Incorrect username or password'})


def login_get_authenticator(request):
    if request.method == 'GET':
        r = requests.get('http://models-api:8000/api/v1/auths')


def log_out(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/api/v1/delete_auth', request.POST)
        return JsonResponse(r.json())
    return JsonResponse({'ok': False, 'result': 'Incorrect request method'})


def search(request):
    if request.method == 'POST':
        es = Elasticsearch(['es'])
        search_results = es.search(index='listing_index', body={'query': {'query_string': {'query': request.POST.get('query')}}, 'size': 10})

        search = search_results['hits']['hits']
        search2 = []
        for item in search:
            search2.append(item['_source'])

        return JsonResponse({'ok': True, 'result': search2})

    return render(request, 'web/search.html', {'form': form_class})
