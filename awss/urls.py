from django.urls import path
from . import views
app_name = 'awss'

urlpatterns = [
    path('', views.home, name='awss-home'),
    path('service/', views.service, name='awss-service'),
    path('about/', views.about, name='awss-about'),
    path('contact/', views.contact, name='awss-contact'),
    path('login/', views.signin, name='awss-login'),
    path('signup/', views.signup, name='awss-signup'),
    path('scan/', views.scan, name='awss-scan'),
    path('signout/', views.signout, name='awss-signout'),
]
