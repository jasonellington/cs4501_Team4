from django.http import JsonResponse
from .models import User, Car, Buyers, Sellers, Authenticator
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import hashers
import os
import hmac
import operator
from django.conf import settings


def home_page(request):
    return render(request, '/web/homePage.html')


def details(request):
    return render(request, '/web/details.html')


def register(request):
    return render(request, '/web/register.html')


def get_users(request):
    if request.method == 'GET':
        results = {}

        for user in User.objects.all():
            results[user.user_id] = {'first_name': user.first_name, 'last_name': user.last_name, 'user_id': user.user_id, 'age': user.age, 'rating': user.rating}

        response = {'ok': True, 'result': results}

        return JsonResponse(response)


def get_user_id(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(user_id=user_id)
            return JsonResponse({'ok': True, 'user_id': user_id})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'user does not exist', 'user_id': user_id})


def check_auth(request, authenticator):
    if request.method == 'GET':
        try:
            auth = Authenticator.objects.get(authenticator=authenticator)
            return JsonResponse({'authenticator': authenticator})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'Authenticator does not exist', 'authenticator': authenticator})


def get_password(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(user_id=user_id)
            return JsonResponse({'ok': True, 'password': user.password})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'user does not exist', 'user_id': user_id})


def get_user(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=user_id)
            return JsonResponse({'ok': True, 'result': {'id': user_id, 'first_name': user.first_name, 'last_name': user.last_name, 'user_id': user.user_id, 'age': user.age, 'rating': user.rating}})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'user does not exist', 'id': user_id})


@csrf_exempt
def update_user(request, id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            if request.POST.get('first_name'):
                user.first_name = request.POST.get('first_name')
            if request.POST.get('last_name'):
                user.last_name = request.POST.get('last_name')
            if request.POST.get('user_id'):
                user.user_id = request.POST.get('user_id')
            if request.POST.get('password'):
                user.password = request.POST.get('password')
            if request.POST.get('age'):
                user.age = request.POST.get('age')
            if request.POST.get('rating'):
                user.rating = request.POST.get('rating')

            user.save()
            results = {'first_name': user.first_name, 'last_name': user.last_name, 'user_id': user.user_id, 'password': user.password, 'age': user.age, 'rating': user.rating}

            return JsonResponse({'ok': True, 'result': results})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'no user exists with that id'})


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        if request.POST.get('user_id'):
            user_id = request.POST.get('user_id')
        if request.POST.get('first_name'):
            first_name = request.POST.get('first_name')
        if request.POST.get('last_name'):
            last_name = request.POST.get('last_name')
        if request.POST.get('password'):
            password = hashers.make_password(request.POST.get('password'))
        if request.POST.get('age'):
            age = request.POST.get('age')
        if request.POST.get('rating'):
            rating = request.POST.get('rating')

        try:
            u = User.objects.get(user_id=user_id)
            return JsonResponse({'ok': False, 'result': 'user_id already in use'})

        except ObjectDoesNotExist:
            user = User(user_id=user_id, first_name=first_name, last_name=last_name, password=password, age=age, rating=rating)
            result = user.save()

            results = {'user_id': user_id, 'first_name': first_name, 'last_name': last_name, 'password': password, 'age': age, 'rating': rating}

            return JsonResponse({'ok': True, 'result': results})


@csrf_exempt
def delete_user(request, id):
    if request.method == 'DELETE':
        user = User.objects.get(id=user_id)
        user.delete()

        return JsonResponse({'ok': True, 'user_id': user_id, 'result': 'user deleted'})


def get_cars(request):
    if request.method == 'GET':
        results = {}

        for car in Car.objects.all():
            results[car.id] = {'make': car.make, 'car_model': car.car_model, 'year': car.year, 'color': car.color, 'body_type': car.body_type, 'num_seats': car.num_seats, 'date_created': car.date_created}

        response = {'ok': True, 'result': results}

        return JsonResponse(response)


def get_car(request, car_id):
    if request.method == 'GET':
        try:
            car = Car.objects.get(id=car_id)
            return JsonResponse({'ok': True, 'result': {'id': car_id, 'make': car.make, 'car_model': car.car_model, 'year': car.year, 'color': car.color, 'body_type': car.body_type, 'num_seats': car.num_seats, 'date_created': car.date_created}})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'car does not exist', 'id': car_id})


@csrf_exempt
def update_car(request, id):
    if request.method == 'POST':
        try:
            car = Car.objects.get(id=id)
            if request.POST.get('make'):
                car.make = request.POST.get('make')
            if request.POST.get('car_model'):
                car.car_model = request.POST.get('car_model')
            if request.POST.get('year'):
                car.year = request.POST.get('year')
            if request.POST.get('color'):
                car.color = request.POST.get('color')
            if request.POST.get('body_type'):
                car.body_type = request.POST.get('body_type')
            if request.POST.get('num_seats'):
                car.num_seats = request.POST.get('num_seats')

            car.save()
            results = {'make': car.make, 'car_model': car.car_model, 'year': car.year, 'color': car.color, 'body_type': car.body_type, 'num_seats': car.num_seats}

            return JsonResponse({'ok': True, 'result': results})

        except ObjectDoesNotExist:
            return JsonResponse({'ok': False, 'result': 'no car exists with that id'})


@csrf_exempt
def create_car(request):
    if request.method == 'POST':
        if request.POST.get('make'):
            make = request.POST.get('make')
        if request.POST.get('model'):
            model = request.POST.get('model')
        if request.POST.get('year'):
            year = request.POST.get('year')
        if request.POST.get('color'):
            color = request.POST.get('color')
        if request.POST.get('body_type'):
            body_type = request.POST.get('body_type')
        if request.POST.get('num_seats'):
            num_seats = request.POST.get('num_seats')

        date_created = int(datetime.utcnow().timestamp())

        car = Car(make=make, car_model=model, year=year, color=color, body_type=body_type, num_seats=num_seats, date_created=date_created)
        car.save()

        car2 = Car.objects.get(date_created=date_created)
        results = {'id': car2.id, 'make': car2.make, 'car_model': car2.car_model, 'year': car2.year, 'color': car2.color, 'body_type': car2.body_type, 'num_seats': car2.num_seats, 'date_created': car2.date_created}

        return JsonResponse({'ok': True, 'result': results})


@csrf_exempt
def delete_car(request, id):
    if request.method == 'DELETE':
        car = Car.objects.get(id=id)
        car.delete()

        return JsonResponse({'ok': True, 'id': id, 'result': 'car deleted'})


def delete_auth(request):
    authenticator = request.POST.get('authenticator')
    auth = Authenticator.objects.get(authenticator=authenticator)
    auth.delete()

    return JsonResponse({'ok': True, 'id': authenticator, 'result': 'auths deleted'})


def get_recently_added_cars(request):
    if request.method == 'GET':
        results = {}

        for car in Car.objects.all():
            results[car.id] = car.date_created

        sorted_dates = sorted(results.items(), key=operator.itemgetter(1))
        sorted_dates.reverse()

        response = {'ok': True, 'result': sorted_dates[:3]}

        return JsonResponse(response)


@csrf_exempt
def add_auth(request):
    if request.method == 'POST':
        if request.POST.get('user_id'):
            user_id = request.POST.get('user_id')
            date_created = int(datetime.utcnow().timestamp())
            authenticator = hmac.new(key=settings.SECRET_KEY.encode('utf-8'), msg=os.urandom(32), digestmod='sha256').hexdigest()
            auth = Authenticator(user_id=user_id, authenticator=authenticator, date_created=date_created)
            auth.save()
            results = {'user_id': user_id, 'authenticator': authenticator, 'date_created': date_created}
            return JsonResponse({'ok': True, 'result': results})

    return JsonResponse({'ok': False, 'result': 'Incorrect method or incorrect user_id'})


def get_auths(request):
    if request.method == 'GET':
        results = {}

        for auth in Authenticator.objects.all():
            results[auth.user_id] = {'user_id': auth.user_id, 'authenticator': auth.authenticator,'date_created': auth.date_created}

        response = {'ok': True, 'result': results}

        return JsonResponse(response)
