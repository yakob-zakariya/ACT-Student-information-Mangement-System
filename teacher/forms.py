from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class SubmitMarksForm(forms.Form):
    mid_exam_result = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)],
        widget=forms.NumberInput(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        })
    )

    class_assessment = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        widget=forms.NumberInput(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        })
    )

    final_exam_result = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        widget=forms.NumberInput(attrs={
            'class': 'border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md font-bold'
        })
    )
