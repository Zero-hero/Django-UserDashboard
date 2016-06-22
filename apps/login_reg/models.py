from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	pass

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
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