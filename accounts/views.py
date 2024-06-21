from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import User 
from school.models import Department,Batch



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
                return render(request,'accounts/login.html',{'form':form})
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    user = request.user 
    if user.role == "REGISTRAR":
        students = User.objects.filter(role="STUDENT")
        return render(request,'registrars/index.html')
    elif user.role == "ADMIN":
        students = User.objects.filter(role="STUDENT").count()
        registrars = User.objects.filter(role="REGISTRAR").count()
        departments = Department.objects.all().count()
        teachers = User.objects.filter(role="TEACHER").count()
        return render(request,'adminApp/index.html',{'students':students,'registrars':registrars,'departments':departments,'teachers':teachers})
    elif user.role == "DEPARTMENT_HEAD":
        batches = Batch.objects.filter(department=request.user.department_head.department)
    
        
        return render(request,'departmentHead/index.html',{'batches':batches})
    
