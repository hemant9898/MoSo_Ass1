from django.db import models

# Create your models here.


class Account(models.Model):
	name = models.CharField(max_length=100)
	follower_count = models.IntegerField()
	following_count = models.IntegerField()
	genre = models.CharField(max_length=200,blank=True)
	bio = models.CharField(max_length=300,blank=True)
	city = models.CharField(max_length=200,blank=True)
	contact_details = models.CharField(max_length=100,blank=True)


	def __str__(self):
		return str(self.name)