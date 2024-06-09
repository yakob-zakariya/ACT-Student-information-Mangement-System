from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# def login_view(request):
#     if request.method=="POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             print(username,password)
#             user = authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 if user.role=="STUDENT":
#                     return redirect("student-dashboard")
#                 elif user.role=="REGISTRAR":
#                     return redirect("registrar-dashboard")
#                 elif user.role=="DEPARTMENT_HEAD":
#                     return redirect('coordinator-dashboard')
#                 elif user.role=="TEACHER":
#                     return redirect('teacher-dashboard')
#                 elif user.role=='ADMIN':
#                     return redirect('admin-dashboard')
#                 return redirect('index')
#             else:
#                 form.add_error(None, "Invalid username or password.")
#                 return render(request,'accounts/login.html',{'form':form})
                
#     else:
#         form = LoginForm()
#         return render(request,'accounts/login.html',{'form':form})


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
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    user = request.user 
    if user.role == "REGISTRAR":
        return render(request,'registrars/index.html')
    elif user.role == "ADMIN":
        return render(request,'adminApp/index.html')
