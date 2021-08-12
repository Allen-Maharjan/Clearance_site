from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from accounts.models import *
from accounts.decorators import allowed_users, admin_only


@login_required(login_url='Login')
@allowed_users(allowed_roles=['Student'])
def underConstruction(request):

    info = Clearance.objects.filter(name=request.user)

    context = {'info': info}

    return render(request, 'SecondHome.html', context)


@login_required(login_url='Login')
@admin_only
def userPage(request):

    return render(request,
                  'UserView.html', {})


def form_print(request):

    info = Clearance.objects.filter(name=request.user)
    context = {'info': info}

    return render(request, 'FormPrint.html', context)
