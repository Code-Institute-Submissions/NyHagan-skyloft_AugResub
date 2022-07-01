from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.beat, name='beat'),
]