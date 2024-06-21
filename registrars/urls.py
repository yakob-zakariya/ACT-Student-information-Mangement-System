from django.urls import path 
from . import views 

urlpatterns = [
    path('departments/',views.departments,name='departments'),
    path('batches/<int:pk>/',views.batches,name='batches'),
    path('batches/create/',views.create_batch,name='create_batch'),
    path('batches/delete/<int:batch_id>/',views.delete_batch,name='delete_batch'),
    path('batches/<int:pk>/sections/',views.sections,name='sections'),
    path('batches/<int:pk>/sections/create/',views.create_section,name='create_section'),
    
    path('batches/<int:pk>/students/',views.students_of_batch,name='students_of_batch'),    
    path('sections/<int:pk>/students/',views.students_of_section,name='students_of_section'),

    path('students/create/',views.create_student,name='create_student'),
    path('select_section/<int:student_id>/',views.assign_section,name='assign_section'),
    path('students/delete/<int:pk>/',views.delete_student,name='delete_student'),
    
    
    path('profile/',views.profile,name='profile'),
    
    path('export/pdf/<int:pk>/', views.download_students_pdf, name='export_pdf'),
    
]
