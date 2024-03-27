from django.shortcuts import render
from .models import Pet,PetPreference,AdoptionApplication,MeetAndGreet,Service

# Create your views here.
def home(request):
    pet =Pet.objects.all()
    context= {
        'pet' : pet,
    }

    return render(request,template_name='home.html',context=context)

def Services(request):
    return render(request,template_name='Services.html')

def About_Us(request):
    return render(request,template_name='About Us.html')

def Contact(request):
    return render(request,template_name='Contact.html')

def login(request):
    return render(request,template_name='login.html')

def Sign_Up(request):
    return render(request,template_name='Sign Up.html')



