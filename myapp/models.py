from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	user_name = models.CharField(max_length=30)
	age = models.IntegerField()
	rating = models.IntegerField()

class Car(models.Model):
	make = models.CharField(max_length=30)
	car_model = models.CharField(max_length=30)
	year = models.IntegerField()
	color = models.CharField(max_length=30)
	body_type = models.CharField(max_length=30)
	num_seats = models.IntegerField()    

class Buyers(models.Model):
	user_id = models.CharField(max_length=30)

class Sellers(models.Model):
	user_id = models.CharField(max_length=30)
	day_avail = models.CharField(max_length=30) 
	time_avail = models.CharField(max_length=30) 
	day_due = models.CharField(max_length=30) 
	time_due = models.CharField(max_length=30) 

 	
