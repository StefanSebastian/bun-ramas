from django.db import models
from django.contrib.auth.models import User

'''
Consumer user model
Describes a consumer user profile
'''
class Consumer(models.Model):
	'''
	Reference
	'''
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	'''
	String representation of the object
	Returns the user name
	'''
	def __str__(self):
		return self.user.username;
