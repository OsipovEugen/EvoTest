from django.db import models
from django.shortcuts import reverse

class Person(models.Model):
	email = models.EmailField(max_length=100)

