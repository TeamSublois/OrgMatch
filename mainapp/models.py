from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=2)
    
    def __str__(self):
        return self.abbreviation


class Category(models.Model):
    name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='mainapp/images/category/')

    def __str__(self):
        return self.name


class Organization(models.Model):
  name = models.CharField(max_length=30)
  bio = models.CharField(max_length=140)
  profile_picture = models.ImageField(upload_to='mainapp/images/organization/', max_length=100, blank=True)
  city = models.CharField(max_length=30)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  categories = models.ManyToManyField(Category)
  minimum_time_commitment = models.IntegerField(default=10, blank=True)
  facebook = models.URLField(null=True, blank=True)
  twitter = models.URLField(null=True, blank=True)
  youtube = models.URLField(null=True, blank=True)
  instagram = models.URLField(null=True, blank=True)

  def __str__(self):
      return self.name


class Event(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=280)
    date = models.DateTimeField()
    event_image = models.ImageField(upload_to='mainapp/images/event/', max_length=100, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=140)
    profile_picture = models.ImageField(upload_to='mainapp/images/volunteer/', max_length=100, blank=True)
    city = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    category_list = models.ManyToManyField(Category)
    fav_org_list = models.ManyToManyField(Organization, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

