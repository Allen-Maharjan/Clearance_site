from django.urls import path

from .views import simple_form

urlpatterns = [
    path('home/', simple_form),
]
