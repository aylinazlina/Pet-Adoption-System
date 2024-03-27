from django.contrib import admin
from .models import Pet,PetPreference,AdoptionApplication,MeetAndGreet,Service

# Register your models here.
admin.site.register([Pet,PetPreference,AdoptionApplication,MeetAndGreet,Service])

