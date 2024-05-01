"""
URL configuration for pasystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from pets import views as p_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', p_view.home, name='home'),
    path('ServicesAdoption/',p_view.Services_Adoption,name='ServicesAdoption'),
    path(' /<str:id>',p_view.pet_details,name ='petdetails'),
    path('upload_pet/',p_view.upload_pet,name='upload_pet'),
    path('update/<str:id>',p_view.update,name='update'),
    path('delete/<str:id>',p_view.delete,name='delete'),
    path('Vaccination/',p_view.Vaccination,name='Vaccination'),
    path('Foster/',p_view.Foster,name='Foster'),
    path('MeetAndGreet/',p_view.Meet_and_Greet,name='MeetAndGreet'),
    path('AboutUs/',p_view.About_Us,name='AboutUs'),
    path('Contact/',p_view.Contact,name='Contact'),
    path('login/',p_view.loginPage,name='login'),
    path('logout/', p_view.logoutUser, name='logout'),

    path('SignUp/',p_view.Sign_Up,name='SignUp')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
