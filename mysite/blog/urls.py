from django.urls import path

from . import views # the '.' means current directory

urlpatterns = [
    path('', views.index, name='index')
]