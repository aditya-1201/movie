from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    first_name 		= models.CharField(max_length=100)
    last_name 		= models.CharField(max_length=100)
    user_name 		= models.CharField(max_length=100)
    password 		= models.CharField(max_length=100)
    mobile 			= models.BigIntegerField()
    email 			= models.EmailField(max_length=100)


class Movie(models.Model):
	movie_name 		= models.CharField(max_length=120)
	release_date 	= models.DateField()
	director 		= models.CharField(max_length=120)
	writers 		= models.CharField(max_length=120)
	stars 			= models.CharField(max_length=120)
	description 	= models.CharField(max_length=255)
	picture			= models.ImageField(upload_to='movies/pictures',max_length=255,null=True,blank=True)
	# file 			= models.FileField()