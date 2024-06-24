from django.urls import path 
from . import views

urlpatterns = [
    path('courses',views.courses,name='courses'),
    path('add-course/',views.add_course,name='add_course'),
    path('delete-course/<int:pk>/',views.delete_course,name='delete-course'),
    path('allocate-course/',views.allocate_course,name='allocate-course'),
    # path('',coordinator_dashboard,name='coordinator-dashboard'),
    # path('batches',batches,name='batches'),
    path('batch/<int:pk>/',views.batch_detail,name='batch-detail'),
    path('delete-batch-course/<int:batch_id>/<int:semester_id>/<int:course_id>/',views.delete_batch_course,name='delete-batch-course'),
    path('select-semester/',views.select_semester,name='select_semester'),
    path('section-teacher/<int:semester_id>/<int:section_id>/',views.section_teacher,name='section_teacher'),
    path('assign-teacher/<int:section_teacher_id>/',views.assign_teacher,name='assign-teacher'),
    
    # path('allocate-teacher',allocate_teacher,name='allocate-teacher'),
    
    # path('students',students,name='cor-students'),
    # path('add-section/<int:pk>',add_section,name='add-section'),
    # path('assign-section/<int:pk>',assign_section,name='assign-section'),
    # path('teacher-courses',teacher_courses,name='teacher-courses'),
    
]
