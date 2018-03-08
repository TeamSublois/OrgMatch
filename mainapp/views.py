from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, VolunteerForm


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


# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 # return HttpResponse("Account not active")
#                 return HttpResponseRedirect(reverse('mainapp:user_login'))
#         else:
#             print("someone tried to login and failed")
#             print("Username: {} and password {}:".format(username, password))
#             # return HttpResponse("invalid login details supplied")
#             # return HttpResponseRedirect(reverse('mainapp:user_login'))
#             messages.error(request,'username or password not correct')
#             return redirect('mainapp:user_login')
#     else:
#         return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    user = request.user
    context = {'user': user}

    return render(request, 'special.html', context)
