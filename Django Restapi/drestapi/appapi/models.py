from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=120)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=120)

	def __str__(self):
		return self.username

class Person(models.Model):	
	fullname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	mobile = models.CharField(max_length=11)
	message = models.CharField(max_length=255)
	userid = models.CharField(max_length=255)

	def __str__(self):
		return self.fullname
