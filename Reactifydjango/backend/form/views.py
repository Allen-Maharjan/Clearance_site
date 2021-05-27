from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.response import Response

from .models import Login


@csrf_exempt
def simple_form(request):

    if (request.method == 'GET'):
        form = Login()
        return render(request,
                      'index.html', {})

    elif (request.method == 'POST'):
        form = Login(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_name)
            return HttpResponse("OK")
        else:
            return HttpResponse("hello")
