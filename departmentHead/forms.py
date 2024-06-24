from django.forms  import ModelForm 
from django import forms 
from school.models import Course,Department,AcademicYear,Section
from accounts.models import TeacherUser 

# class AddCourse(ModelForm):
    
#     class Meta:
#         model=Course;
#         fields = "__all__"

class AddCourse(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    code = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    credit_hour = forms.IntegerField(
    widget=forms.NumberInput(attrs={
        'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
    }))
    
    prerequisites = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        })
    )
    
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        })
    )


    
    


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
            
            
class SelectSemester(forms.Form):
    section = forms.ModelChoiceField(
        queryset=Section.objects.none(), 
        widget=forms.Select(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        }))
    academic_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        widget=forms.Select(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        }))
    
    
    semester_choice = [("One","One"),("Two","Two")]
    
    semester = forms.ChoiceField(choices=semester_choice,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SelectSemester, self).__init__(*args, **kwargs)

        if user:
            # Filter the section by user's department
            self.fields['section'].queryset = Section.objects.filter(batch__department=user.department_head.department)
    
    
   
class SelectTeacher(forms.Form):
     teacher = forms.ModelChoiceField(
        queryset=TeacherUser.teachers.all(),
        widget=forms.Select(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        }))
    
     

# class TeacherAllocateForm(forms.Form):
#     academic_years = AcademicYear.objects.all()
#     a_choices = []
#     for academic in academic_years:
#         a_choices.append((academic.id,academic.name))
   
#     semester_choice = [("One","One"),("Two","Two")]
    
#     academic_year = forms.ChoiceField(choices=a_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
#     semester = forms.ChoiceField(choices=semester_choice,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    
#     batches = forms.ChoiceField()
    
#     def __init__(self, *args, **kwargs):
#         batch_choices = kwargs.pop('batch_choices', None)
#         section_choices = kwargs.pop('section_choices', None)
#         super(TeacherAllocateForm, self).__init__(*args, **kwargs)
        
#         if batch_choices:
#             self.fields['batches'] = forms.ChoiceField(choices=batch_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
#         if section_choices:
#             self.fields['sections'] = forms.ChoiceField(choices=section_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
            
    
#     TEACHER_CHOICES = [(teacher.id,teacher.username) for teacher in Teacher.teachers.all()]
#     teacher = forms.ChoiceField(choices=TEACHER_CHOICES,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
#     COURSE_CHOICES = [(course.id,course.name) for course in Course.objects.all()]
#     course = forms.ChoiceField(choices=COURSE_CHOICES,widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
    

    
# class AssignSection(forms.Form):
#     def __init__(self, *args, **kwargs):
#         section_choices = kwargs.pop('section_choices', None)
#         super(AssignSection, self).__init__(*args, **kwargs)
    
#         if section_choices:
#             self.fields['section'] = forms.ChoiceField(choices=section_choices, widget=forms.Select(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold ml-0'}))
        
# class AddSection(forms.Form):
#     section_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))