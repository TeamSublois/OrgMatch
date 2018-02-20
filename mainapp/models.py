from django.db import models

class Volunteer(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='mainapp/static/mainapp/images/', max_length=100)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=2)

  def __str__(self):
      return self.first_name + " " + self.last_name


class Organization(models.Model):
  name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='mainapp/static/mainapp/images/', max_length=100)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=2)

  def __str__(self):
      return self.name