from django.contrib import admin

from .models import Volunteer, Organization, State, Category

admin.site.register(Volunteer)
admin.site.register(Organization)
admin.site.register(State)
admin.site.register(Category)
