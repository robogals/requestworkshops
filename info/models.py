from django.db import models


CHAPTER_LIST = (
	(0, 'Robogals Melbourne'),
	(1, 'Robogals Monash (Melbourne)'),
	(2, 'Robogals Adelaide'),
	(3, 'Robogals Auckland'),
	(4, 'Robogals Brisbane'),
	(5, 'Robogals Canberra'),
	(6, 'Robogals Hobart'),
	(7, 'Robogals Newcastle'),
	(8, 'Robogals Perth'),
	(9, 'Robogals Sydney'),
	(10, 'Robogals Toowoomba')
)


# Model for the requesting school's information
class SchoolRequestInformation(models.Model):
	school_name = models.CharField(max_length=100, default='')
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	mobile = models.CharField(max_length=100, default='')
	email = models.EmailField()
	school_address = models.CharField(max_length=100, default='')
	school_city = models.CharField(max_length=100, default='')
	school_postcode = models.CharField(max_length=8, default='')
	position = models.CharField(max_length=100)
	chapter = models.IntegerField(choices=CHAPTER_LIST, default=0)
	permission_to_contact = models.BooleanField(default=0)
	sent = models.BooleanField(default=0)