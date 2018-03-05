from django.contrib import admin

from .models import Volunteer, Organization, State, Category, Event

admin.site.register(Volunteer)
admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Event)