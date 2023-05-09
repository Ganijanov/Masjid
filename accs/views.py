from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def loginForAdmin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        chek = authenticate(username=username, password=password)
        if chek is not None:
            login(request, chek)
            return redirect('mp_url')
        else:
            return redirect('mp_url')
        

def  logoutForAdmin(request):
    logout(request)
    return redirect('mp_url')