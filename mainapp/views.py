from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from .forms import UserForm, VolunteerForm


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


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

    # context = RequestContext(request, context)

    # template = loader.get_template('register.html')
    return render(request, 'register.html', context)
    # return HttpResponse(template.render(context))
