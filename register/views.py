from asyncio.windows_events import NULL
from dataclasses import field
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from .models import Child


# Create your views here.
def register(request):
    if request.method == 'POST':
        image = request.POST['image']
        surname = request.POST['surname']
        other_name = request.POST['other']
        D_o_B = request.POST['dob']
        LGA = request.POST['LGA']
        state = request.POST['state']
        Sex = request.POST['sex']
        home_address = request.POST['home_address']
        previous_school = request.POST['previous_school']
        previous_class = request.POST['previous_class']
        from_date = request.POST['from_date']
        to = request.POST['to']
        father = request.POST['father']
        occupation_father = request.POST['occupy']
        mobile_father = request.POST['mobile_father']
        email_father = request.POST['email_father']
        mother = request.POST['mother']
        occupation_mother = request.POST['occupation']
        mobile_mother = request.POST['mobile_mother']
        email_mother = request.POST['email_mother']
        immunized = request.POST['rad']
        medical_certificate = request.POST['photo']
        hearing_difficulty = request.POST['hear']
        doctor_consultation = request.POST['doc']
        Explain = request.POST['explain ']
        vision = request.POST['eye']
        spectacles = request.POST['spec']
        any_illness = request.POST['ill']
        description = request.POST['describe']

      

        Student = Child(image=image, surname=surname, other=other_name, birth_date=D_o_B, LGA=LGA, State=state,
                            Gender=Sex, Address1=home_address, previous_school=previous_school, previous_class=previous_class,
                            from_date=from_date, to=to, father=father, mother=mother, occupation_father=occupation_father, occupation_mother=occupation_mother, mobile_father=mobile_father, mobile_mother=mobile_mother,
                            email_father=email_father,email_mother=email_mother,immunized=immunized,medical_certificate=medical_certificate,hearing_difficulty=hearing_difficulty,doctor_consultation=doctor_consultation,explain=Explain,
                            vision=vision,spectacles=spectacles,any_illness=any_illness,description=description )
        Student.save()
                
    return render(request, 'register.html')


