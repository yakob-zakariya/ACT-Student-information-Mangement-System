from django.shortcuts import render,redirect
from .forms import BatchCreationForm,AddSection,StudentRegisterForm,SectionForm
from school.models import Department,Batch,Section
from accounts.models import Student,StudentUser
from django.contrib import messages
from accounts.decorators import registrar_required
from django.contrib.auth.decorators import login_required



@login_required
@registrar_required
def departments(request):
    departments = Department.objects.all()
    return render(request,'registrars/departments.html',{'departments':departments})

@login_required
@registrar_required
def batches(request,pk):
    department = Department.objects.get(pk=pk)
    batches = Batch.objects.filter(department=department)
    return render(request,'registrars/batches.html',{'batches':batches,'department':department})


def create_batch(request):
    if request.method== "POST":
        form = BatchCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            department = int(form.cleaned_data['department'])
            print("this department " + str(department))
            Batch.objects.create(name=name,department_id=department)
            messages.success(request,"Batch created successfully")
            return redirect('batches',pk=department)
    else:
        form = BatchCreationForm()
    return render(request,'registrars/create_batch.html',{'form':form})

def delete_batch(request,batch_id):
    batch = Batch.objects.get(pk = batch_id)
    department_id = batch.department.id
    batch.delete()
    return redirect('batches',department_id)   

   
def sections(request,pk):
    batch = Batch.objects.get(pk=pk)
    sections = batch.sections.all()
    return render(request,'registrars/sections.html',{'sections':sections,'batch':batch})  

def create_section(request,pk):
    batch = Batch.objects.get(pk =pk)
    if request.method == "POST":
        form = AddSection(request.POST)
        if form.is_valid():
            section_name = form.cleaned_data['section_name']
            batch.sections.create(name=section_name)
            messages.success(request,"Section created successfully")
            return redirect('sections',pk=batch.id)
    else:
        form = AddSection()
    return render(request,'registrars/create_section.html',{'form':form})


def create_student(request):
    if request.method=="POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            middle_name=form.cleaned_data['middle_name']
            last_name=form.cleaned_data['last_name']
            dep_id = int(form.cleaned_data['department'])
            batch_id = int(form.cleaned_data['batch'])
            email = form.cleaned_data['email']
            
            department = Department.objects.get(pk = dep_id)
            batch = Batch.objects.get(pk = batch_id)
            batch_suffix = batch.name[2:]
            student = StudentUser.objects.create_student_user(batch_suffix)
            student.first_name=first_name
            student.middle_name=middle_name
            student.email=email
            student.last_name=last_name
            student.save()
            Student.objects.create(student=student,department=department,batch=batch)
            messages.success(request,f"Student {first_name}  {middle_name} {last_name} is registered successfully")
            return redirect('students_of_batch',batch.id)
    else:  
        form = StudentRegisterForm()
    return render(request,'registrars/create_student.html',{'form':form})


def delete_student(request,pk):
    student = StudentUser.objects.get(pk = pk)
    batch_id = student.student.batch.id
    student.delete()
    return redirect(students_of_batch,batch_id)

def students_of_batch(request,pk):
    batch = Batch.objects.get(pk=pk)
    students = StudentUser.objects.filter(student__batch=batch)
    print(students)
    return render(request,'registrars/students_of_batch.html',{'students':students,'batch':batch})

def students_of_section(request,pk):
    section = Section.objects.get(pk = pk)
    students = StudentUser.objects.filter(student__section=section)
    return render(request,'registrars/students_of_section.html',{'students':students,'section':section})

def profile(request):
    return render(request,'registrars/profile.html')

def assign_section(request,student_id):
    student = StudentUser.objects.get(pk = student_id)
    student_data = student.student
    batch_id = student.student.batch.id 
    if request.method == "POST":
        form = SectionForm(request.POST,batch_id = batch_id)
        if form.is_valid():
            selected_section = form.cleaned_data['section']
            student_data.section = selected_section
            student_data.save()
            return redirect('students_of_section',selected_section.id)
            
    else:
        form = SectionForm(batch_id=batch_id)
    return render(request,'registrars/assign_section.html',{'form':form})

# views.py

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .utils import export_students_to_pdf  # Assuming this is where your PDF generation utility is located

def download_students_pdf(request,pk):
    
    # Get the section object
    section = Section.objects.get(pk = pk)
    
    # Retrieve department and batch from the section object
    department_name = section.batch.department.name
    batch = section.batch.name
    section_name = section.name
    print("before calling export")
    # Generate the PDF file
    pdf_file_path = export_students_to_pdf(department_name, batch, section)
    print("after calling export")

    # Serve the PDF file as a download
    with open(pdf_file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="students_{section_name}.pdf"'
        return response





