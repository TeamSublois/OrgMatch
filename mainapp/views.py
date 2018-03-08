from django.http import HttpResponse
from django.template import Context, loader
from .models import Organization
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, VolunteerForm
from .models import Category, Organization


def index(request):
    user = request.user
    context = {'user': user}

    return render(request, 'home.html', context)


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

    return render(request, 'register.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    user = request.user
    context = {'user': user}

    return render(request, 'special.html', context)


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
