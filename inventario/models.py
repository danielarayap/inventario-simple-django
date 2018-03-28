from django.db import models
from django.utils import timezone
from datetime import datetime

class Product(models.Model):
	producto = models.CharField(max_length=255)
	amount = models.PositiveSmallIntegerField(default=5)
	pub_date = models.DateTimeField('date published', null=True, blank=True, default=datetime.now)
	def __str__(self):
		return self.producto


