from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Service(models.Model):
    S_id = models.IntegerField(blank=True, null=True)
    S_choice = (
        ('Adoption', 'Adoption'),
        ('MeetAndGreet', 'MeetAndGreet'),
        ('Vaccination', 'Vaccination'),
    )
    status = models.CharField(max_length=100, choices=S_choice, blank=True, null=True)

    def _IntegerField_(self):
        return self. S_id


class PetPreference(models.Model):
    id = models.IntegerField(primary_key=True)

    species_choice = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
    )
    species = models.CharField(max_length=100, choices=species_choice, blank=True, null=True)
    bread = models.TextField(max_length=200, null=True)
    age = models.IntegerField(blank=True, null=True)
    size_choice = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    size = models.CharField(max_length=100, choices=size_choice, blank=True, null=True)
    description = models.TextField(max_length=200, null=True)
    adoptionFee = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True,default='images/default.jpg')

    def __str__(self):
        return self.bread


class Adoption(models.Model):
    PetPreference = models.ForeignKey(PetPreference, on_delete=models.CASCADE, blank=True, null=True)

    availability_choice = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),

    )
    Availability = models.CharField(max_length=100, choices=availability_choice, blank=True, null=True)


class MeetAndGreet(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    PetPreference = models.ForeignKey(PetPreference, on_delete=models.CASCADE, blank=True, null=True)
    scheduledAt = models.DateTimeField(auto_now_add=True,auto_now=False)
    location = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.location

class Vacci(models.Model):
    Pet_Category_choice = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
    )
    Pet_Category = models.CharField(max_length=100, choices= Pet_Category_choice, blank=True, null=True)
    BookingAppointment = models.DateTimeField(auto_now_add=True,auto_now=False)
    Type = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.Type


class Fostering(models.Model):
    Condition_choice = (
        ('Healthy', 'Healthy'),
        ('Sick', 'Sick'),

    )
    Condition = models.CharField(max_length=100, choices= Condition_choice, blank=True, null=True)

    AccomodationAvailablity_choice = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),

    )
    AccomodationAvailablity= models.CharField(max_length=100, choices= AccomodationAvailablity_choice, blank=True, null=True)

    Reqeust_choice = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    Reqeust= models.CharField(max_length=100, choices= Reqeust_choice, blank=True, null=True)














