from django.db import models

class User(models.Model):
	user_id = models.CharField(max_length=30, primary_key=True)
	password = models.CharField(max_length=150)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField()
	rating = models.IntegerField()

class Car(models.Model):
	id = models.AutoField(primary_key=True)
	make = models.CharField(max_length=30)
	car_model = models.CharField(max_length=30)
	year = models.IntegerField()
	color = models.CharField(max_length=30)
	body_type = models.CharField(max_length=30)
	num_seats = models.IntegerField()
	date_created = models.IntegerField()

class Buyers(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.CharField(max_length=30)

class Sellers(models.Model):
	user_id = models.CharField(max_length=30)
	car_id = models.CharField(max_length=30)
	day_avail = models.IntegerField()
	time_avail = models.IntegerField()
	day_due = models.IntegerField()
	time_due = models.IntegerField()

class Authenticator(models.Model):
	user_id = models.CharField(max_length=30)
	authenticator = models.CharField(max_length=100,primary_key=True)
	date_created = models.IntegerField()
	