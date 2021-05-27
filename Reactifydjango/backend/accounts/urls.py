from django.urls import path

from .views import registerPage, loginPage, logoutUser

urlpatterns = [
    path('Login/', loginPage, name='Login'),
    path('Register/', registerPage, name='Register'),
    path('Logout/', logoutUser, name='Logout'),

]
