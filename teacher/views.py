from django.shortcuts import render,redirect
from school.models import Section_teacher,Registration,Semester,Section,Course,CourseGrades
from .forms import SubmitMarksForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import teacher_required 


@login_required
@teacher_required
def teacher_students(request,semester_id,section_id,course_id):
    teacher = request.user
    semester = Semester.objects.get(id=semester_id)
    section = Section.objects.get(id=section_id)
    course = Course.objects.get(id = course_id)
    registration_students = Registration.objects.filter(teacher=teacher,course=course,semester=semester,student__student__section=section)
    return render(request,'teacher/teacher_students.html',{'registration_students':registration_students,'course':course,"semester":semester,"section":section})

@login_required
@teacher_required
def submit_marks(request,registration_id):
    registration = Registration.objects.get(id=registration_id)
    semester = registration.semester
    section = registration.student.student.section
    course = registration.course
    print(semester.id,section.id,course.id)
    if request.method == 'POST':
        form = SubmitMarksForm(request.POST)
        if form.is_valid():
            mid_exam_result = float(form.cleaned_data['mid_exam_result'])
            class_assessment = float(form.cleaned_data['class_assessment'])
            final_exam_result = float(form.cleaned_data['final_exam_result'])
            
            course_grades = CourseGrades.objects.create(registration=registration,mid_exam_result=mid_exam_result,class_assessment=class_assessment,final_exam_result=final_exam_result)
            return redirect("teacher_students",semester.id,section.id,course.id)
    else:
        form = SubmitMarksForm()
        print(semester.id,section.id,course.id)
    return render(request,'teacher/submit_marks.html',{'form':form})
