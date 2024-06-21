# from django.shortcuts import render,redirect
# from school.models import Batch,Batch_course,AcademicYear,Semester,Section_teacher,Section,Course
# from accounts.models import Student,StudentUser,Teacher
# from .forms import CourseAllocate,TeacherAllocateForm,AssignSection,AddSection
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from accounts.decorators import department_head_required


# @login_required
# def coordinator_dashboard(request):
#     batches = Batch.objects.filter(department=request.user.coordinator_profile.department)
    
#     return render(request,'coordinator/coordinator_dashboard.html',{'batches':batches})
    
    
 
# @login_required
# def batches(request):
#     batches = Batch.objects.filter(department=request.user.coordinator_profile.department)
#     return render(request,'coordinator/batches.html',{'batches':batches})

# @login_required
# def batch_detail(request,pk):
#     batch = Batch.objects.get(pk=pk)
#     sections = batch.sections.all()
    
#     semesters = Semester.objects.order_by('-id')
#     semester_courses = {}
#     for semester in semesters:
#         # Fetch courses for the current semester
#         courses = Batch_course.objects.filter(semester=semester,batch=batch)
        
#         # Store courses in the dictionary
#         semester_courses[semester] = courses
    
    
#     return render(request,'coordinator/batch_detail.html',{'batch':batch,'semester_courses':semester_courses,'sections':sections})


# @login_required
# def allocate_course(request):
#     batches = Batch.objects.filter(department=request.user.coordinator_profile.department)
#     BATCH_CHOICE = [(b.id,f"batch of {b.name}") for b in batches]
#     if request.method=="POST":
#         form = CourseAllocate(request.POST,batch_choices=BATCH_CHOICE)
#         if form.is_valid():
#             batch = Batch.objects.get(pk=int(form.cleaned_data['batches']))
#             academic_year_id = int(form.cleaned_data['academic_year'])
#             print(academic_year_id)
#             academic_year_ob = AcademicYear.objects.get(pk = academic_year_id)
            
#             semester= Semester.objects.get(name=form.cleaned_data['semester'],AcademicYear=academic_year_ob)
#             print(semester.id,semester.name,semester.AcademicYear,batch)
#             courses = form.cleaned_data['courses']
            
#             for course in courses:
#                 Batch_course.objects.create(batch=batch,course=course,semester=semester)
#             return redirect('coordinator-dashboard')
            
            
#     else:
#         form = CourseAllocate(batch_choices=BATCH_CHOICE)
#     return render(request,'coordinator/course_allocation.html',{'form':form})




# @login_required
# def allocate_teacher(request):
#     batches = Batch.objects.filter(department=request.user.coordinator_profile.department)
#     sections = Section.objects.filter(batch__in=batches)
#     print(sections)
#     BATCH_CHOICE = [(b.id,f"batch of {b.name}") for b in batches]
    
#     SECTION_CHOICE = [(s.id,f"{s.name}({s.batch.name})") for s in sections]
    
#     if request.method == "POST":
#         form = TeacherAllocateForm(batch_choices=BATCH_CHOICE,section_choices=SECTION_CHOICE,data=request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             academic_year = AcademicYear.objects.get(pk=form.cleaned_data['academic_year'])
#             semester = Semester.objects.get(name=form.cleaned_data['semester'],AcademicYear=academic_year)
#             batch = Batch.objects.get(pk=form.cleaned_data['batches'])
#             section = Section.objects.get(pk=form.cleaned_data['sections'])
#             teacher = Teacher.objects.get(pk = form.cleaned_data['teacher'])
#             print(teacher)
#             course = Course.objects.get(pk=form.cleaned_data['course'])
#             Section_teacher.objects.create(teacher=teacher,section=section,semester=semester,course=course)
#             return redirect('coordinator-dashboard')
#     else:
#         form = TeacherAllocateForm(batch_choices=BATCH_CHOICE,section_choices=SECTION_CHOICE)
    
#     return render(request,'coordinator/allocate_teacher.html',{'form':form})

# @login_required
# def students(request):
#     students = Student.objects.filter(student_profile__department=request.user.coordinator_profile.department)
#     return render(request,'coordinator/students.html',{'students':students})

# def assign_section(request,pk):
#     student = Student.objects.get(pk=pk)
#     sections = Section.objects.filter(batch__department=request.user.coordinator_profile.department,batch=student.student_profile.batch)
#     SECTION_CHOICE = [(s.id,f"{s.name}({s.batch.name})") for s in sections]
    
#     if request.method == "POST":
#         form = AssignSection(data=request.POST,section_choices=SECTION_CHOICE)
#         if form.is_valid():
#             print(form.cleaned_data)
#             section = Section.objects.get(pk = int(form.cleaned_data['section']))
#             print("****",section.name,section.batch.name)
#             student_profile = StudentProfile.objects.get(student=student)
#             student_profile.section=section
#             student_profile.save()
#             return redirect('students')
#     else:
#         form = AssignSection(section_choices=SECTION_CHOICE)
#     return render(request,'coordinator/assign_section.html',{'form':form})


# def add_section(request,pk):
#     batch = Batch.objects.get(pk = pk)
#     if request.method == "POST":
#         form = AddSection(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             section = Section.objects.create(name=form.cleaned_data['section_name'],batch=batch)
#             messages.success(request,'Section is created Successfully')
#             return redirect('batch-detail',pk=batch.id)
#     else:
#         form = AddSection()
#     return render(request,'coordinator/add_section.html',{'form':form,'batch':batch})

# def teacher_courses(request):
#     teacher_courses = Section_teacher.objects.all()
#     return render(request,'coordinator/teacher_courses.html',{"teacher_courses":teacher_courses})
    