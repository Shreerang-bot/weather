from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
     path('about.html', views.about, name='about'),
]
