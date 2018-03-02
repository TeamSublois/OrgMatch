from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import Category, Organization


def index(request):
    all_categories_list = Category.objects.order_by('name')[:3]
    context = {'all_categories_list':all_categories_list}
    
    return render(request, 'mainapp/home.html', context)


def category(request):
	all_categories_list = Category.objects.order_by('name')[:1000]
	context = {'all_categories_list':all_categories_list}

	return render(request, 'mainapp/category.html', context)