from django.shortcuts import render,redirect
from .models import Service,PetPreference,Adoption,MeetAndGreet,Vacci

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# Create your views here.

@login_required(login_url='login')
def home(request):

    return render(request,template_name='home.html')

@login_required(login_url='login')
def Services_Adoption(request):
    pet = PetPreference.objects.all()
    context = {
        'pet': pet,
    }
    return render(request,template_name='Services_Adoption.html',context=context)

@login_required(login_url='login')
def Vaccination(request):
    vac = Vacci.objects.all()
    context = {
        'Vacc': vac,
    }
    return render(request,template_name='Vaccination.html',context=context)

def upload_pet(request):
    form =AddPetForm()
    if request.method =='POST':
        form = AddPetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ServicesAdoption')
    context ={
        'form' : form,
    }
    return render(request,template_name='upload_pet.html',context=context)
def update(request):
    petp=PetPreference.objects.get(pk = id)
    form = AddPetForm(instance=petp)
    if request.method =='POST':
        form = AddPetForm(request.POST,instance=petp)
        if form.is_valid():
            form.save()
            return redirect('ServicesAdoption')
    context ={
        'form' : form,
    }
    return render(request,template_name='upload_pet.html',context=context)
def delete(request):
    petp = PetPreference.objects.get(pk=id)

    if request.method =='POST':
        petp.delete()
        return redirect('ServicesAdoption')

    return render(request,template_name='delete.html')

def pet_details(request,id):
    petp =PetPreference.objects.get(pk = id)
    context = {
        'petpre' : petp,
    }
    return render(request,template_name='pet_details.html',context =context)
@login_required(login_url='login')
def Foster(request):
    fos = Fostering.objects.all()
    context = {
        'Fost' : fos,
    }
    return render(request,template_name='Foster.html',context=context)

@login_required(login_url='login')
def Meet_and_Greet(request):
    meet = MeetAndGreet.objects.all()
    context = {
        'MG' : meet,
    }
    return render(request,template_name='Meet_and_Greet.html',context=context)
@login_required(login_url='login')
def About_Us(request):
    return render(request,template_name='About Us.html')
@login_required(login_url='login')
def Contact(request):
    return render(request,template_name='Contact.html')


def Sign_Up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for' + user)
                return redirect('login')
        context ={
            'form': form,
        }
        return render(request,template_name='Sign Up.html',context=context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username OR password is incorrect')


    return render(request,template_name='login.html')
def logoutUser(request):
    logout(request)
    return redirect('login')


