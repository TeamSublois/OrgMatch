from django.urls import path

from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('recommended/', views.recommended, name='recommended')
]