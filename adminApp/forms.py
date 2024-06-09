from django import forms 

class AddUser(forms.Form):
    user_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter User Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter First Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    middle_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Middle Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'placeholder':'Enter Email Address','class':'border rounded w-full py-3 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'}))
    
    

    