from django.urls import path

from .views import underConstruction, form_print
from .api_view import (
    ClearanceModelCreateApiView,
    ClearanceModelDestroyApiView,
    ClearanceModelListApiView,
    ClearanceModelRetrieveAPIView,
    ClearanceModelUpdateAPIView)

urlpatterns = [
    path('UnderConstruction/', underConstruction, name='underconstruction'),
    path('PrintFrom/', form_print, name='form_print'),
    path('generic/create', ClearanceModelCreateApiView.as_view()),
    path('generic/list/', ClearanceModelListApiView.as_view()),
    path('generic/delete/<int:pk>', ClearanceModelDestroyApiView.as_view()),
    path('generic/update/<int:pk>', ClearanceModelUpdateAPIView.as_view()),
    path('generic/detail/<int:pk>', ClearanceModelRetrieveAPIView.as_view()),
]
