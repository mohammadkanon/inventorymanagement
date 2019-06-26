from django.db import models

# Create your models here.
class Device(models.Model):
	type = models.CharField(max_length=100, blank=False)
	price = models.IntegerField()

	choices =(
		('AVAILABLE', 'Item is ready to purchased'),
		('SOLD', 'Item sold'),
		('RESTOCKING', 'Item restocking in few days')
	)

	status = models.CharField(max_length=10, choices=choices, default='Sold')
	issuse = models.CharField(max_length=100, default='No Issue')

	class Meta:
		abstract = True

	def __str__(self):
		return '%s %s' % (self.type, self.price)

class Laptop(Device):
	pass

class Desktop(Device):
	pass

class Mobile(Device):
	pass