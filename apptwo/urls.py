from django.urls import path, include
from apptwo import views

urlpatterns = [
    path('', views.get_users, name='users'),
]
