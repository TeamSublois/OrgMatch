from django.http import HttpResponse
from django.template import Context, loader
from .models import Organization
from django.shortcuts import render

def index(request):
	template = loader.get_template('mainapp/index.html')
	return HttpResponse(template.render())

def results(request):

	all_organizations_list = Organization.objects.order_by('city')[:5]
	context = {'all_organizations_list': all_organizations_list,}
	
	return render(request, 'mainapp/results.html', context)