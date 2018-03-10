from django.http import HttpResponse
from django.template import Context, loader
from .models import Organization
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, VolunteerForm
from .models import Category, Organization
from django.db import connection


def db(request):

    cursor = connection.cursor()
    cursor.execute('select mainapp_organization.name, mainapp_category.name from mainapp_organization, mainapp_organization_categories INNER JOIN mainapp_category on mainapp_organization_categories.category_id = mainapp_category.id')
    rows = []
    for row in cursor.fetchall():
        rows.append(row)

    i = 1
    org1cats = []
    cursor.execute('select mainapp_organization.name, mainapp_category.name from mainapp_organization, mainapp_organization_categories INNER JOIN mainapp_category on mainapp_organization_categories.category_id = mainapp_category.id where mainapp_organization.id = ' + str(i))
    for cat in cursor.fetchall():
        org1cats.append(cat)

    i = 2
    org2cats = []
    cursor.execute('select mainapp_organization.name, mainapp_category.name from mainapp_organization, mainapp_organization_categories INNER JOIN mainapp_category on mainapp_organization_categories.category_id = mainapp_category.id where mainapp_organization.id = ' + str(i))
    for cat in cursor.fetchall():
        org1cats.append(cat)

    user2cats = []
    cursor.execute('select mainapp_category.name as catname from mainapp_volunteer, mainapp_volunteer_category_list INNER JOIN mainapp_category on mainapp_volunteer_category_list.category_id = mainapp_category.id where user_id = ' + str(i) + ' ORDER BY catname')
    for cat in cursor.fetchall():
        user2cats.append(cat)


    context = {
        'rows': rows,
        'org1cats': org1cats,
        'org2cats': org2cats,
        'user2cats': user2cats,
    }

    return render(request, 'mainapp/db.html', context)


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        volunteer_form = VolunteerForm(data=request.POST)

        if user_form.is_valid() and volunteer_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            volunteer = volunteer_form.save(commit=False)
            volunteer.user = user
            volunteer.save()
            registered = True

        else:
            print(user_form.errors, volunteer_form.errors)

    else:
        user_form = UserForm()
        volunteer_form = VolunteerForm()

    context = {
                'user_form': user_form,
                'volunteer_form': volunteer_form,
                'registered': registered,
                }

    return render(request, 'mainapp/register.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    all_categories_list = Category.objects.order_by('name')[:3]
    context = {'all_categories_list':all_categories_list}

    return render(request, 'mainapp/home.html', context)


def recommended(request):

    all_organizations_list = Organization.objects.order_by('city')[:100]
    context = {'all_organizations_list': all_organizations_list,}

    return render(request, 'mainapp/recommended.html', context)


def category(request):
    all_categories_list = Category.objects.order_by('name')

    context = {
        'all_categories_list':all_categories_list
    }

    return render(request, 'mainapp/category.html', context)
