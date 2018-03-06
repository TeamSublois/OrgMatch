from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import Category, Organization


def index(request):
    all_categories_list = Category.objects.order_by('name')[:3]
    context = {'all_categories_list':all_categories_list}
    
    return render(request, 'mainapp/home.html', context)


def category(request):
	all_categories_list = Category.objects.order_by('name')

	first_col = all_categories_list[0:int(len(all_categories_list)/3)]
	second_col = all_categories_list[int(len(all_categories_list)/3):int(2*(len(all_categories_list)/3))]
	third_col = all_categories_list[int(2*(len(all_categories_list)/3)):]

	context = {
		'all_categories_list':all_categories_list,
		'first_col':first_col,
		'second_col':second_col,
		'third_col':third_col
	}

	return render(request, 'mainapp/category.html', context)