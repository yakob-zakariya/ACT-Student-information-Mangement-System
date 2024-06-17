from django import forms 
from school.models import Department,AcademicYear

class AddDepartment(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter Department Name','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    code =forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Department code','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
class AddUser(forms.Form):
    user_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter User Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter First Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    middle_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Middle Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'placeholder':'Enter Email Address','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    

   
class AddDepartmentHead(forms.Form):
    user_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter User Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter First Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    middle_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Middle Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'placeholder':'Enter Email Address','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    departments = Department.objects.all()
    
    department_choices = []

    for dep in departments:
        department_choices.append((dep.id,dep.name))
    

    department = forms.ChoiceField(choices=department_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))




class AddAcademicYear(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Academic Year Name','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    start_date=forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Enter Start Date','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    end_date=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter End Date','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
   
class AddSemester(forms.Form):
    academic_years = AcademicYear.objects.all()
    ACADEMIC_YEAR_CHOICE = [(y.id,y.name) for y in academic_years]
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Semester Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    academic_year = forms.ChoiceField(choices=ACADEMIC_YEAR_CHOICE,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    start_date=forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Enter Start Date','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    end_date=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter End Date','class':'border rounded w-full py-4 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    


    