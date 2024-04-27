from django.contrib import admin
from .models import PetPreference,Adoption,MeetAndGreet,Service,Vacci,Fostering

# Register your models here.
admin.site.register([PetPreference,Adoption,MeetAndGreet,Service,Vacci,Fostering])

