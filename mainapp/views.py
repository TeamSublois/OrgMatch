from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from .models import Organization

def index(request):
	template = loader.get_template('mainapp/index.html')
	return HttpResponse(template.render())

def organization(request, id):
	template = loader.get_template('mainapp/org.html')
	org = get_object_or_404(Organization, pk=id)
	return render(request, 'mainapp/org.html', {"org": org})