from django.urls import path 
from . import views 


urlpatterns = [
    path('choose-semester/',views.choose_registration_semester,name='choose-semester'),
    path('course-register/<int:pk>/',views.course_register,name='course-register'),
     path('registered-course/',views.registered_courses,name="registered-courses"),
     
     path('grade-report',views.grade_reports,name='grade-report'),
     path('update-profile',views.update_profile,name='update-profile'),
     
     path('delete',views.temp,name='delete-registration')
     
    
    
]
