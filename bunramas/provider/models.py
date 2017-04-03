from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

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
	Starting Date - DateTimeField
	The offer's starting date
	Defaults to current datetime
	'''
	starting_date = models.DateTimeField(default = timezone.now);

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

	'''
	Slug for URL reversing.
	'''
	slug = models.SlugField(max_length = 250, default = "");

	'''
	String representation of the object
	Returns the title
	'''
	def __str__(self):
		return self.title;

	'''
	Validates an object
	'''
	def clean(self):
		if (self.expiration_date is not None) and (self.starting_date >= self.expiration_date):
			raise ValidationError({'expiration_date':'Expiration date must be after starting date!'})

	'''
	Returns the slugified corresponding title of the Offer.
	'''
	# def slug(self):
	# 	return slugify(self.title)

	def __init__(self, *args, **kwargs):
		super(Offer, self).__init__(*args, **kwargs)
		self.slug = slugify(self.title)
