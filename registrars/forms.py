from django import forms 
from school.models import Department,Batch,Section 
class BatchCreationForm(forms.Form):
    departments = Department.objects.all()
    batches = Batch.objects.order_by('-id')
    department_choices = []
    batch_choices = []
    for dep in departments:
        department_choices.append((dep.id,dep.name))
        
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Batch Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
     
    department = forms.ChoiceField(choices=department_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
        
class AddSection(forms.Form):
    section_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))



class StudentRegisterForm(forms.Form):
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter First Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    middle_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Middle Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'placeholder':'Enter Email Address','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    departments = Department.objects.all()
    batches = Batch.objects.order_by('-id')
    department_choices = []
    batch_choices = []
    for dep in departments:
        department_choices.append((dep.id,dep.name))
    
    for batch in batches:
        batch_choices.append((batch.id,f"{batch.name}({batch.department.code})"))
    department = forms.ChoiceField(choices=department_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    batch = forms.ChoiceField(choices=batch_choices,widget=forms.Select(attrs={'class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
class SectionForm(forms.Form):
     section = forms.ModelChoiceField(
        queryset=Section.objects.none(),
        label='Select Section',
        widget=forms.Select(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        }))
     def __init__(self, *args, **kwargs):
        batch_id = kwargs.pop('batch_id', None)
        super(SectionForm, self).__init__(*args, **kwargs)
        if batch_id:
            self.fields['section'].queryset = Section.objects.filter(batch_id=batch_id)