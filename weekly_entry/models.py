

from django.db import models
from users.models import CustomUser

# Models



class Student(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    # Student Base Info
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)



    date_of_birth = models.DateField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

   
    
    def __str__(self): 
        return "%s %s" % (self.first_name , self.last_name)


class WeeklyEntry(models.Model):
    SYMPTOM_CHOICES = (
        ('I Feel Fine', 'I Feel Fine'),
        ('I could be better', 'I could be better'),
        ('I have had a fever', 'I have had a fever'),
    )
    AVG_PEOPLE = (
        ('0-5', '0-5 People'),
        ('6-15', '6-15 People'),
        ('16-20+', '16-20+ People'),
    )
    DINING_HALL = (
        ('In Dining Hall', 'Have Eaten in Dining Hall'),
        ('Not In Dining Hall', 'Have Eaten in Room'),
        ('Eaten Off Campus', 'Have Eaten Off Campus'),
    )
    LEFT_CAMPUS = (
        ('Y', 'Have Left Campus'),
        ('N', 'Have Not Left Campus'),
    )
    

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_symptoms = models.CharField(max_length=400, choices=SYMPTOM_CHOICES)
    avg_people_seen = models.CharField(max_length=200, choices=AVG_PEOPLE)
    dining_hall = models.CharField(max_length=200, choices=DINING_HALL)
    leave_campus = models.CharField(max_length=200, choices=LEFT_CAMPUS)


    def __str__(self): 
        return "Current Symptoms: %s, Average People Seen in the Past Week: %s, Eating: %s, Have you left campus: %s " %(self.current_symptoms, self.avg_people_seen, self.dining_hall, self.leave_campus)
