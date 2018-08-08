from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.

def add_user(request):
    return render(request, 'add_user.html')

def list_user(request):
    users = User.objects.filter(is_superuser=False).all()

    return render(request, 'list_user.html', {'users': users})