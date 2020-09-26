

from django.db import models
from users.models import CustomUser

# Models



class Student(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    # Pilot Base Info
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200)



    date_of_birth = models.DateField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Contact
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    # Address

    STATE_CHOICES = (("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming"))

    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
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
