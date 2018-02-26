from django.contrib.postgres.fields import ArrayField
from django.db import models


class State(models.Model):
    abbreviation = models.CharField(max_length=2)
    
    def __str__(self):
        return self.abbreviation


class Category(models.Model):
    name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='static/mainapp/images/')

    def __str__(self):
        return self.name


class Organization(models.Model):
  name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='static/mainapp/images/', max_length=100, blank=True)
  city = models.CharField(max_length=30)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  categories = models.ManyToManyField(Category)
  time_commitement = ArrayField(models.IntegerField(default=10), size=2)
  events = ArrayField(models.CharField(default="", max_length=20, blank=True))

  def __str__(self):
      return self.name


class Volunteer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=140)
    profile_picture = models.ImageField(upload_to='static/mainapp/images/', max_length=100, blank=True)
    city = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    category_list = models.ManyToManyField(Category)
    fav_org_list = models.ManyToManyField(Organization, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

