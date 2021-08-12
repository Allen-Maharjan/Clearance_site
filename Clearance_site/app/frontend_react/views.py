from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_only


@login_required(login_url="Login")
@admin_only
def index(request):
    return render(request, 'frontend/index.html')
