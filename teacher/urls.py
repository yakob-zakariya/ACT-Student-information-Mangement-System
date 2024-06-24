from django.urls import path 

from . import views 

urlpatterns = [
    path('teacher-students/<int:semester_id>/<int:section_id>/<int:course_id>/',views.teacher_students,name='teacher_students'),
    path('submit-marks/<int:registration_id>/',views.submit_marks,name='submit_marks')
]
