from __future__ import unicode_literals
from ..login_reg.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
	message = models.TextField()
	wall = models.ForeignKey(User, related_name = "wall")
	user = models.ForeignKey(User, related_name = "user")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.message
	class Meta:
		db_table = "messages"

class Comment(models.Model):
	comment = models.TextField()
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.comment
	class Meta:
		db_table = "comments"