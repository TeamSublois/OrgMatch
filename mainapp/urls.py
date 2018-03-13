from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('recommended/', views.recommended, name='recommended'),
    path('category/', views.category, name='category'),
    path('org/<int:id>', views.organization, name='org'),
    path('volunteer/<int:id>', views.volunteer, name='volunteer')
]
