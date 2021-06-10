
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('acc/', include('accounts.urls')),

    path('verified/', include('afterLogin.urls')),

    path('user/', include('frontend_react.urls')),

    path('', include('home.urls')),

    path('superuser/', include('update.urls')),
]
