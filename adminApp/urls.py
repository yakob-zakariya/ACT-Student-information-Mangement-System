from django.urls import path 
from . import views
urlpatterns = [
    path('add-registrar/',views.add_registrar,name='add-registrar'),
    path('registrars',views.registrars,name='registrars'),
]

