from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from apptwo.models import User

def index(request):
    return render(request, 'apptwo/index.html')


def get_users(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {'users': users_list} 
    
    return render(request, 'apptwo/users.html', context=users_dict)
