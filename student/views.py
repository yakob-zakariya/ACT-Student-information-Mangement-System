from django.shortcuts import render,redirect
from .forms import ChooseRegistrationSemester,SelectCourseForm
from school.models import Batch_course,AcademicYear,Semester,Registration,Course,Section_teacher
from django.db.models import Q
from accounts.models import StudentUser
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required

@login_required
@student_required
def choose_registration_semester(request):
    if request.method=="POST":
        form = ChooseRegistrationSemester(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            academic_id = form.cleaned_data.get('academic_year')
            semester_name = form.cleaned_data.get('semester')
            academic_yearOb = AcademicYear.objects.get(pk = int(academic_id))
            semester_obj = Semester.objects.get(AcademicYear=academic_yearOb,name=semester_name)
            sem_id = semester_obj.id
            batch = request.user.student.batch
            courses = Batch_course.objects.filter(batch=batch,semester=semester_obj)
            
            if courses.count()==0:
                return redirect('no-registration')
            elif Registration.objects.filter(semester=semester_obj,student=request.user):
                print("yes there is ",sem_id)
                return redirect('registered-courses')
            
            
            return redirect('course-register',pk=sem_id)
    else:
        form = ChooseRegistrationSemester()
    return render(request,'student/choose_semester.html',{'form':form})


@login_required
@student_required
def no_registration(request):
    return render(request,'student/no_registration.html')


@login_required
@student_required
def course_register(request,pk):
    batch = request.user.student.batch
    semester = Semester.objects.get(pk=pk)
    courses_allocated = Batch_course.objects.filter(batch=batch, semester=semester)
    course_ids = [course.course_id for course in courses_allocated]
    
    # Convert list of course IDs to a queryset
    course_queryset = Course.objects.filter(Q(id__in=course_ids))
    
    if request.method == "POST":
        form = SelectCourseForm(request.POST, queryset=course_queryset)
        if form.is_valid():
            print(form.cleaned_data)
            selected_courses = form.cleaned_data.get('courses')
            student = request.user
            section = student.student.section
            
            for course in selected_courses:
                if Section_teacher.objects.filter(course=course,semester=semester,section=section):
                    teacher = Section_teacher.objects.get(course=course,semester=semester,section=section).teacher 
                    Registration.objects.create(student=student, course=course, semester=semester,teacher=teacher)
                else:
                    Registration.objects.create(student=student, course=course, semester=semester)
                
            return redirect('registered-courses')
    else:
        form = SelectCourseForm(queryset=course_queryset)  # Pass queryset here
    
    return render(request, 'student/course_register.html', {'form': form})


@login_required
@student_required
def registered_courses(request):
    student = StudentUser.objects.get(pk=request.user.id)
    semesters = Semester.objects.order_by('-id')
    semester_courses = {}
    for semester in semesters:
        # Fetch courses for the current semester
        courses = Registration.objects.filter(semester=semester,student=student)
        
        # Store courses in the dictionary
        semester_courses[semester] = courses
    
    
    return render(request,'student/registered_courses.html',{'semester_courses':semester_courses,})

@login_required
@student_required
def grade_reports(request):
    student = StudentUser.objects.get(pk=request.user.id)
    semesters = Semester.objects.order_by('-id')
    semester_courses = {}
    for semester in semesters:
        # Fetch courses for the current semester
        courses = Registration.objects.filter(semester=semester,student=student)
        
        # Store courses in the dictionary
        semester_courses[semester] = courses
    
    
    return render(request,'student/grade_report.html',{'semester_courses':semester_courses,})



        
def update_profile(request):
    return render(request,'student/update_profile.html')
      
 #  bad function temporary used to delete ## for testing
def temp(request):
    Registration.objects.all().delete()
    Section_teacher.objects.all().delete()
    Batch_course.objects.all().delete()
    return redirect('home')