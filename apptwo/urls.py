from django.urls import path, include
from apptwo import views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('signup/', views.show_form, name='signup'),

]
