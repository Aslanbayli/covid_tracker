

from django import forms
from .models import Student
from .models import WeeklyEntry


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 
            'last_name',
            'last_name' ,
            'gender',
            'phone',
            'email',
]



class WeeklyEntryForm(forms.ModelForm):
    class Meta:
        model = WeeklyEntry
        fields = [
            'student',

        ]






        