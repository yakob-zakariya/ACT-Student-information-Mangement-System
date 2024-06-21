from django import forms 
from users.models import Batch_course,Course,AcademicYear,Semester,Teacher

class CourseAllocate(forms.Form):
    academic_years = AcademicYear.objects.all()
    a_choices = []
    for academic in academic_years:
        a_choices.append((academic.id,academic.name))
   
    semester_choice = [("One","One"),("Two","Two")]
    
    academic_year = forms.ChoiceField(choices=a_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    semester = forms.ChoiceField(choices=semester_choice,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    
    batches = forms.ChoiceField()
    
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class':'rounded-sm'}),
        label='Select Courses'
    )
    
    def __init__(self, *args, **kwargs):
        batch_choices = kwargs.pop('batch_choices', None)
        super(CourseAllocate, self).__init__(*args, **kwargs)
        
        if batch_choices:
            self.fields['batches'] = forms.ChoiceField(choices=batch_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
            
            


class TeacherAllocateForm(forms.Form):
    academic_years = AcademicYear.objects.all()
    a_choices = []
    for academic in academic_years:
        a_choices.append((academic.id,academic.name))
   
    semester_choice = [("One","One"),("Two","Two")]
    
    academic_year = forms.ChoiceField(choices=a_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    semester = forms.ChoiceField(choices=semester_choice,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    
    batches = forms.ChoiceField()
    
    def __init__(self, *args, **kwargs):
        batch_choices = kwargs.pop('batch_choices', None)
        section_choices = kwargs.pop('section_choices', None)
        super(TeacherAllocateForm, self).__init__(*args, **kwargs)
        
        if batch_choices:
            self.fields['batches'] = forms.ChoiceField(choices=batch_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
        if section_choices:
            self.fields['sections'] = forms.ChoiceField(choices=section_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
            
    
    TEACHER_CHOICES = [(teacher.id,teacher.username) for teacher in Teacher.teachers.all()]
    teacher = forms.ChoiceField(choices=TEACHER_CHOICES,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    COURSE_CHOICES = [(course.id,course.name) for course in Course.objects.all()]
    course = forms.ChoiceField(choices=COURSE_CHOICES,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    

    
class AssignSection(forms.Form):
    def __init__(self, *args, **kwargs):
        section_choices = kwargs.pop('section_choices', None)
        super(AssignSection, self).__init__(*args, **kwargs)
    
        if section_choices:
            self.fields['section'] = forms.ChoiceField(choices=section_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
        
class AddSection(forms.Form):
    section_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))