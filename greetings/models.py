from django.db import models
from django.shortcuts import reverse

class Person(models.Model):
	email = models.EmailField(max_length=100)
	
	# def get_absolute_url(self):
 #   		return reverse('yes_url')


	# def get_absolute_url(self):
	# 	return reverse('yes_url')



# Create your models here.
