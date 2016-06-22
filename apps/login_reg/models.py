from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
	def register(self, first_name, last_name, email, password, conf_password):
		errors = {}

		try:
			self.all()
		except:
			admin_user = 1

		try:
			admin_user
		except:
			admin_user = 0
		if len(first_name) < 2 or not NAME_REGEX.match(first_name):
			errors['first_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(last_name) < 2 or not NAME_REGEX.match(last_name):
			errors['last_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(email) < 1:
			errors['req_email'] = "Email is required"
		if not EMAIL_REGEX.match(email):
			errors['email'] = "Email not valid"
		if len(password) < 8:
			errors['password'] = "Password must be atleast 8 characters"
		if password != conf_password:
			errors['confirm_password'] = "passwords do not match"
		if errors:
			return (False, errors)


		else:
			password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
			self.create(first_name=first_name, last_name=last_name, email=email, password=password, role = admin_user)
			return (True, self.get(email=email))

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	role = models.IntegerField(default=0)
	email = models.EmailField()
	password = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()
	def __str__(self):
		return self.first_name
	class Meta:
		db_table = "users"