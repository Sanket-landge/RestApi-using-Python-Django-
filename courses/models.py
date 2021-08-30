from django.db import models

class Courses(models.Model):
	name = models.CharField(max_length = 80)
	language = models.CharField(max_length = 80)
	price = models.CharField(max_length = 10)

	def __str__(self):
		return self.name
