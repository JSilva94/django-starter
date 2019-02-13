from django.urls import path, include
from apptwo import views

urlpatterns = [
    path('', views.help, name='users'),
]
