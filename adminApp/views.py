from django.shortcuts import render,redirect
from .forms import AddUser,AddDepartmentHead,AddDepartment,AddAcademicYear,AddSemester
from accounts.models import RegistrarUser,DepartmentHeadUser,DepartmentHead
from django.contrib import messages
from accounts.models import User
from school.models import Department,AcademicYear,Semester
from django.contrib.auth.decorators import login_required


def registrars(request):
    registrars = User.objects.filter(role="REGISTRAR")
    return render(request,'adminApp/registrars.html',{'registrars':registrars})


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
            registrar= RegistrarUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,middle_name=middle_name,email=email,password='1234')
            
            messages.success(request, 'Registrar is  Added Successfully')
            return redirect('registrars')
    else:
        form = AddUser()
    return render(request,'adminApp/add_registrar.html',{"form":form})


def delete_registrar(request,pk):
    registrar = User.objects.get(pk = pk)
    registrar.delete()
    messages.success(request, 'Registrar is  Deleted Successfully')
    return redirect('registrars')


def departments(request):
    departments = Department.objects.all()
    return render(request,'adminApp/departments.html',{'departments':departments})

def add_department(request):
    if request.method == "POST":
        form = AddDepartment(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            code = form.cleaned_data.get('code')
            print(name,code)
            department = Department(name=name,code=code)
            department.save()
            messages.success(request, 'Department is  Added Successfully')
            return redirect('departments')
    else:
        form = AddDepartment()
    return render(request,'adminApp/add_department.html',{"form":form})

def department_heads(request):
    department_heads = User.objects.filter(role="DEPARTMENT_HEAD")
    return render(request,'adminApp/department_heads.html',{'department_heads':department_heads})

def add_department_head(request):
    if request.method == "POST":
        form = AddDepartmentHead(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            print(username,first_name,middle_name,email)
            department_id = int(form.cleaned_data.get('department'))
            department_head= DepartmentHeadUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,middle_name=middle_name,email=email,password='1234')
            
            department = Department.objects.get(pk=department_id)
            department_head_data = DepartmentHead.objects.create(department_head = department_head,department=department)
            
            messages.success(request, 'Department Head is  Added Successfully')
            return redirect('department-heads')
    else:
        form = AddDepartmentHead()
    return render(request,'adminApp/add_department_head.html',{"form":form})

def delete_department_head(request,pk):
    department_head = User.objects.get(pk = pk)
    department_head.delete()
    messages.success(request, 'Department Head is  Deleted Successfully')
    return redirect('department-heads')

def academic_years(request):
    academic_years = AcademicYear.objects.all()
    return render(request,'adminApp/academic_years.html',{'academic_years':academic_years})


@login_required
def add_academic_year(request):
    if request.method == 'POST':
        form = AddAcademicYear(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            print(start_date,end_date)
            AcademicYear.objects.create(name=name, start_date=start_date, end_date=end_date)
            
            messages.success(request, 'Academic Year Added Successfully')
            return redirect('academic-years')
    else:
        form = AddAcademicYear()
    return render(request, 'adminApp/add_academic_year.html', {'form': form})


@login_required
def delete_academic_year(request,pk):
    
    year = AcademicYear.objects.get(pk = pk)
    year.delete()
    messages.success(request,'Academic Year is Delete Successfully')
    return redirect('academic-years')


@login_required
def semesters(request):
    semesters = Semester.objects.all()
    return render(request,'adminApp/semesters.html',{'semesters':semesters})

@login_required
def add_semester(request):
    if request.method=="POST":
        form = AddSemester(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data.get('name')
            academic_year = AcademicYear.objects.get(pk = int(form.cleaned_data.get('academic_year')))
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            Semester.objects.create(name=name,AcademicYear=academic_year,start_date=start_date,end_date=end_date)
            messages.success(request,"A new Semester is Added Successfully")
            return redirect('semesters')            
    else:
        form = AddSemester()
    return render(request,'adminApp/add_semester.html',{'form':form})

    
    

