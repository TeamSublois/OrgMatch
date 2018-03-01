from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import Organization
from .filters import OrgFilter

def index(request):
    template = loader.get_template('mainapp/index.html')
    return HttpResponse(template.render())

def search(request):
	orgs = Organization.objects.all()
	orgFilter = OrgFilter(request.get, queryset = orgs)

	return render(request, "search.html", { "filter" : orgFilter})
