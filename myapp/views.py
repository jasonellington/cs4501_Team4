from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Car, Buyers, Sellers
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home_page(request):
	return JsonResponse({'ok': True, 'result': {}})

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
			u = User.objects.get(id=user_id)
			return JsonResponse({'ok': True, 'result': {'id': user_id, 'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name, 'age': user.age, 'rating': user.rating}})
		
		except ObjectDoesNotExist:
			return JsonResponse({'ok': False, 'result': 'user does not exist', 'id': user_id})

# def create_user(request):
# 	if request.method == 'POST':
# 		form = UserForm(request.POST)
# 		form.setChoices(request)
# 		if form.is_valid():
# 			# create a user object
# 			first_name = request.POST.get('first_name')
# 			last_name = request.POST.get('last_name')
# 			user_name = request.POST.get('user_name')
# 			age = request.POST.get('age')
# 			rating = request.POST.get('rating')

# 			try:
# 				u = User.objects.get(user_name=user_name)
# 				# A user with that user_name already exists - send the form back to user with an error
# 				form = UserForm(request.POST)
# 				form.add_error('user_name', "A user with that username already exists: please try a different username")
				
# 				return render(request, 'myapp/createUser.html', {'form': form})

# 			except ObjectDoesNotExist:
# 				user_obj = User(first_name=first_name, last_name=last_name, user_name=user_name, age=age, rating=rating)
# 				user_obj.save()

# 				#return render(request, 'myapp/userCreated.html', {'ok': True, 'result': {'first_name': first_name, 'last_name': last_name, 'user_name': user_name,'age': age, 'rating': rating}})
# 				return JsonResponse({'ok': True, 'result': {'first_name': first_name, 'last_name': last_name, 'user_name': user_name, 'age': age, 'rating': rating}})
# 	else:
# 		form = UserForm()
# 		form.setChoices(request)
# 	return render(request, 'myapp/createUser.html', {'form': form})




