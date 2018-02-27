from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from .models import Category

def index(request):
    template = loader.get_template('mainapp/index.html')
    return HttpResponse(template.render())
    all_categories_list = Category.objects.order_by('name')[:5]
    context = {'all_categories_list':all_categories_list}
    return render(request, 'mainapp/index.html', context)