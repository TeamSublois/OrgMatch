from django.db import models

class Volunteer(models.Model):

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='uploads/', max_length=100)
  # interest_list
  # org_list
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=2)
  
  # def hash_profile_pic_url(self):
  #   return self

