from django.urls import path

from .views import updateInfo

urlpatterns = [
    path('update/', updateInfo, name='updateinfo')
]
