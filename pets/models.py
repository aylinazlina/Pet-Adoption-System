from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    species_choice = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
    )
    species = models.CharField(max_length=100, choices= species_choice, blank=True, null=True)
    age = models.IntegerField(blank=True,null=True)
    description = models.TextField(max_length=200, null=True)
    adoptionFee = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name

class MeetAndGreet(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE , blank=True,null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    scheduledAt =models.DateTimeField(auto_now_add=False,auto_now=True)
    location= models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.location




class AdoptionApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    submittedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
    status_choice=(
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        )
    status = models.CharField(max_length=100,choices=status_choice,blank = True,null=True)


    def __str__(self):
        return self.status


class PetPreference(models.Model):
    species = models.TextField(max_length=200, null=True)
    bread = models.TextField(max_length=200, null=True)
    size_choice = (
            ('Small', 'Small'),
            ('Medium', 'Medium'),
            ('Large', 'Large'),
        )
    size = models.CharField(max_length=100, choices=size_choice, blank=True, null=True)

    ageRange_choice = (
            ('Puppy', 'Puppy'),
            ('Adult', 'Adult'),
            ('Senior', 'Senior'),
        )
    ageRange = models.CharField(max_length=100, choices=ageRange_choice, blank=True, null=True)


    def __str__(self):
        return self. bread

class Service(models.Model):
    S_id = models.IntegerField(blank=True,null=True)
    S_choice = (
        ('Adoption', 'Adoption'),
        ('MeetAndGreet', 'MeetAndGreet'),
        ('Vaccination', 'Vaccination'),
    )
    status = models.CharField(max_length=100, choices= S_choice, blank=True, null=True)

    def _IntegerField_(self):
        return self. S_id






