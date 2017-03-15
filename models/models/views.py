from django.http import JsonResponse
from .models import User, Car, Buyers, Sellers
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home_page(request):
	return render(request, '/web/homePage.html')

def details(request):
	return render(request, '/web/details.html')


def get_users(request):
	if request.method == 'GET':
		results = {}

		for user in User.objects.all():
			results[user.id] = {'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name, 'age': user.age, 'rating': user.rating}

		response = {'ok': True, 'result': results}

		return JsonResponse(response)

def get_user(request, user_id):
	if request.method == 'GET':
		try:
			user = User.objects.get(id=user_id)
			return JsonResponse({'ok': True, 'result': {'id': user_id, 'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name, 'age': user.age, 'rating': user.rating}})
		
		except ObjectDoesNotExist:
			return JsonResponse({'ok': False, 'result': 'user does not exist', 'id': user_id})

@csrf_exempt
def update_user(request, id):
	if request.method == 'POST':
		try:
			user = User.objects.get(id=id)
			if request.POST.get('first_name'):
				user.first_name = request.POST.get('first_name')
			if request.POST.get('last_name'):
				user.last_name = request.POST.get('last_name')
			if request.POST.get('user_name'):
				user.user_name = request.POST.get('user_name')
			if request.POST.get('age'):
				user.age = request.POST.get('age')
			if request.POST.get('rating'):
				user.rating = request.POST.get('rating')

			user.save()
			results = {'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name, 'age': user.age, 'rating': user.rating}

			return JsonResponse({'ok': True, 'result': results})

		except ObjectDoesNotExist:
			return JsonResponse({'ok': False, 'result': 'no user exists with that id'})

@csrf_exempt
def create_user(request):
	if request.method == 'POST':
		if request.POST.get('id'):
			id = request.POST.get('id')
		if request.POST.get('first_name'):
			first_name = request.POST.get('first_name')
		if request.POST.get('last_name'):
			last_name = request.POST.get('last_name')
		if request.POST.get('user_name'):
			user_name = request.POST.get('user_name')
		if request.POST.get('age'):
			age = request.POST.get('age')
		if request.POST.get('rating'):
			rating = request.POST.get('rating')

		try:
			u = User.objects.get(user_name=user_name)
			return JsonResponse({'ok': False, 'result': 'user_name already in use'})

		except ObjectDoesNotExist:
			user = User(id=id, first_name=first_name, last_name=last_name, user_name=user_name, age=age, rating=rating)
			result = user.save()

			results = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name, 'age': user.age, 'rating': user.rating}

			return JsonResponse({'ok': True, 'result': results, 'result2': result})

@csrf_exempt
def delete_user(request, id):
	if request.method == 'DELETE':
		user = User.objects.get(id=id)
		user.delete()

		return JsonResponse({'ok': True, 'id': id, 'result': 'user deleted'})


def get_cars(request):
	if request.method == 'GET':
		results = {}

		for car in Car.objects.all():
			results[car.id] = {'make': car.make, 'car_model': car.car_model, 'year': car.year, 'color': car.color, 'body_type': car.body_type, 'num_seats': car.num_seats}

		response = {'ok': True, 'result': results}

		return JsonResponse(response)

def get_car(request, car_id):
	if request.method == 'GET':
		try:
			car = Car.objects.get(id=car_id)
			return JsonResponse({'ok': True, 'result': {'id': car_id, 'make': car.make, 'car_model': car.car_model, 'year': car.year, 'color': car.color, 'body_type': car.body_type, 'num_seats': car.num_seats}})
		
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
		if request.POST.get('id'):
			id = request.POST.get('id')
		if request.POST.get('make'):
			make = request.POST.get('make')
		if request.POST.get('car_model'):
			car_model = request.POST.get('car_model')
		if request.POST.get('year'):
			year = request.POST.get('year')
		if request.POST.get('color'):
			color = request.POST.get('color')
		if request.POST.get('body_type'):
			body_type = request.POST.get('body_type')
		if request.POST.get('num_seats'):
			num_seats = request.POST.get('num_seats')

		car = Car(id=id, make=make, car_model=car_model, year=year, color=color, body_type=body_type, num_seats=num_seats)
		car.save()

		results = {'id': car.id, 'make': car.make, 'car_model': car.car_model, 'year': car.year, 'color': car.color, 'body_type': car.body_type, 'num_seats': car.num_seats}

		return JsonResponse({'ok': True, 'result': results})

@csrf_exempt
def delete_car(request, id):
	if request.method == 'DELETE':
		car = Car.objects.get(id=id)
		car.delete()

		return JsonResponse({'ok': True, 'id': id, 'result': 'car deleted'})












