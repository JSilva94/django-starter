from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from apptwo.models import User

def index(request):
    return HttpResponse('<em> My Second App </em>')

def get_users(request):
    users_dict = {'users': User.objects} 
    
    return render(request, 'apptwo/help.html', context=users_dict)
