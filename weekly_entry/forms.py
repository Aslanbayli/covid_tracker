

from django import forms
from .models import Student
from .models import WeeklyEntry


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 
            'middle_name',
            'last_name',
            'last_name' ,
            'date_of_birth' ,
            'gender',
            'phone',
            'email',
            'address1' ,
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
]



class LogbookEntryForm(forms.ModelForm):
    class Meta:
        model = WeeklyEntry
        fields = [
            'pilot',
            'departure_apt',
            'arrival_apt',
            'departure_date',

        ]






        