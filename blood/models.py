from django.db import models
from enum import Enum

# Create your models here.
class Blood(models.Model):
	name = models.CharField(max_length=255)
	year = models.IntegerField()
	email = models.EmailField()
	blood_group = models.CharField(max_length=20)
	corona_status = models.CharField(max_length=100)
	last_checked_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.name

