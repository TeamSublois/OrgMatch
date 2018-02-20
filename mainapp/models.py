from django.contrib.postgres.fields import ArrayField
from django.db import models

class Volunteer(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='static/mainapp/images/', max_length=100, blank=True)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=2)
  category_list = ArrayField(models.CharField(default="", max_length=20, blank=True))
  fav_org_list = ArrayField(models.CharField(default="", max_length=20, blank=True))

  def __str__(self):
      return self.first_name + " " + self.last_name


class Organization(models.Model):
  name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='static/mainapp/images/', max_length=100, blank=True)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=2)
  categories = ArrayField(models.CharField(max_length=20, blank=True))
  time_commitement = ArrayField(models.IntegerField(default=10), size=2)
  events = ArrayField(models.CharField(default="", max_length=20, blank=True))

  def __str__(self):
      return self.name
