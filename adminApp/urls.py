from django.urls import path 
from . import views
urlpatterns = [
    path('',views.admin_home,name='admin-home'),
    # registrar user 
    path('registrars/',views.registrars,name='registrars'),
    path('add-registrar/',views.add_registrar,name='add-registrar'),
    path('delete-registrar/<int:pk>/',views.delete_registrar,name='delete-registrar'),
    
    # departments 
    path('departments/',views.departments,name='admin_departments'),
    path('add-department/',views.add_department,name='add-department'),
    
    # department Heads user
    path('department-heads/',views.department_heads,name='department-heads'),
    path('add-department-head/',views.add_department_head,name='add-department-head'),
    path('delete-department-head/<int:pk>/',views.delete_department_head,name='delete-department-head'),
    
    # academic year
    path('academic-years/',views.academic_years,name='academic-years'),
    path('add-academic-year/',views.add_academic_year,name='add-academic-year'),
    path('delete-academic-year/<int:pk>/',views.delete_academic_year,name='delete-academic-year'),
    
    # semester
    path('semesters/',views.semesters,name='semesters'),
    path('add-semester/',views.add_semester,name='add-semester'),
    
]

