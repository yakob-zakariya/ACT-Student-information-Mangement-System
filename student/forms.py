from django import forms 
from school.models import AcademicYear

class ChooseRegistrationSemester(forms.Form):
    academic_years = AcademicYear.objects.all()
    a_choices = []
    for academic in academic_years:
        a_choices.append((academic.id,academic.name))
   
    semester_choice = [("One","One"),("Two","Two")]
    
    academic_year = forms.ChoiceField(choices=a_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    semester = forms.ChoiceField(choices=semester_choice,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    

class SelectCourseForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=None,  # Set to None initially
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'rounded-sm'}),
        label='Select Courses'
    )
    
    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)  # Pop queryset from kwargs
        super().__init__(*args, **kwargs)
        
        if queryset is not None:
            self.fields['courses'].queryset = queryset 
    