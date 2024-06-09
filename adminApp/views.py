from django.shortcuts import render,redirect
from .forms import AddUser
from accounts.models import Registrar
from django.contrib import messages


def add_registrar(request):
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            print(username,first_name,middle_name,email)
            registrar= Registrar.objects.create_user(username=username,first_name=first_name,last_name=last_name,middle_name=middle_name,email=email,password='1234')
            
            messages.success(request, 'Registrar is  Added Successfully')
            return redirect('registrars')
    else:
        form = AddUser()
    return render(request,'adminApp/add_registrar.html',{"form":form})

def registrars(request):
    return render(request,'adminApp/registrars.html')
