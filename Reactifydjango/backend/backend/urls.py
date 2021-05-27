
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form.urls')),

    path('acc/', include('accounts.urls')),

    path('verified/', include('afterLogin.urls')),

    path('', include('frontend_react.urls')),
]
