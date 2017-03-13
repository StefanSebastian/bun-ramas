from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

'''
Provider user model
Describes a provider user profile
'''
class Provider(models.Model):
	'''
	Reference
	'''
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	'''
	Company name
	'''
	company_name = models.CharField(max_length = 250);

	'''
	String representation of the object
	Returns the company name
	'''
	def __str__(self):
		return self.company_name;

'''
Offer model
Describes an offer made by a provider
'''
class Offer(models.Model):
	'''
	Meta class
	'''
	class Meta:
		'''
		List of permissions for Offer objects
		'''
		permissions = (
			("can_create_offer", "Can create an offer"),
			("can_edit_offer", "Can edit an offer"),
			("can_delete_offer", "Can delete an offer"),
		)

	'''
	Title - CharField
	The title of the offer, visible in offer list
	'''
	title = models.CharField(max_length = 250);

	'''
	Description - TextField
	Contains the offer's details
	'''
	description = models.TextField();

	'''
	Starting Date - DateTimeField
	The offer's starting date
	Defaults to current datetime
	'''
	starting_date = models.DateTimeField(default = datetime.now);

	'''
	Expration Date - DateTimeField
	The offer's expiration date
	'''
	expiration_date = models.DateTimeField();

	'''
	Location - CharField
	Location of the provider
	'''
	location = models.CharField(max_length = 250);

	'''
	Will contain reference to provider
	'''
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

	'''
	String representation of the object
	Returns the title
	'''
	def __str__(self):
		return self.title;
