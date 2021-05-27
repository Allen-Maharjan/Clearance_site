
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .decorators import admin_only, unauthenticated_user, allowed_users, admin_only
from .forms import CreateUserForm
from .models import *
from .CreatingTable import createTable, Student_form

import accounts.templates


@csrf_exempt
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            Student_form(username, email)
            student = Student.objects.get(name=username)
            print(student.id)
            group = Group.objects.get(name='Student')
            user.groups.add(group)
            createTable(student.id, username)

            messages.success(request, 'Account was created for ' + username)
            return redirect('Login')

    context = {'form': form}
    return render(request, 'Register.html', context)


@csrf_exempt
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('UserPage')

        else:
            messages.info(request, 'Username or Password is incorrect')

    form = CreateUserForm
    context = {'form': form}
    return render(request, 'Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('Login')
