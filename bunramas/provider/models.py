from django.db import models

'''
Offer model
Describes an offer made by a provider
'''
class Offer(models.Model):
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
	provider = models.CharField(max_length = 250);
