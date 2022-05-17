

from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth import logout
# from .forms import ParentRegister
# from .models import User


# Create your views here.
def base(request, *args, **kwargs):
    return render(request, "base.html", {})


# Create your views here.
def parent(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password1']
        if password1 == password2:

            if User.objects.filter(email=mail).exists():
                messages.info(request, 'Email Taken')
            elif User.objects.filter(username=name).exists():
                print('username Taken')
            else:
                user = User.objects.create_user(
                    username=name, email=mail, password=password1)
                user.save()
                return redirect("account")

        else:
            messages.error(request, 'password does not match')
        return redirect("parent")

    else:
        return render(request, "parent.html")


def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("base")

        else:
            messages.info(request, 'invalid credentials')
            return redirect("account")

    else:
        return render(request, "login.html")


# def teach(request):
#     return render(request, 'teach-login.html')


# def dashboard(request):
#     return render(request, 'teacher.html')


# def teacher(request):
#     form = TeacherRegister()
#     if request.method == 'POST':
#         form = TeacherRegister(request.POST)
#         if form.is_valid():

#             form.save()

#             return redirect("account")

#     context = {'form': form}
#     return render(request, 'dashreg.html', context)


def logoutUser(request):
    logout(request)
    return redirect("account")


# def teacherlogin(request):
#     # form = TeacherRegister()
#     if request.method == 'POST':
#         form = TeacherRegister(request.POST)
#         if form.is_valid():
#             user = form.update()
#             name = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')

#             user = authenticate(request, email=email, name=name,  password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect("dashboard")

#             else:
#                 messages.info(request, 'invalid credentials')
#                 return redirect("account")

#     else:
#         form = TeacherRegister()
#     return render(request, "teach-login.html")

#     # teacher = Teacherlogin()
#     # if request.method == 'POST':
#     #     email = request.POST.get('email')
#     #     password = request.POST.get('password')

#     #     teacher = auth.authenticate(email=email, password=password)

#     #     if teacher is not None:
#     #         auth.login(request, teacher)
#     #         return redirect("dashboard")

#     #     else:
#     #         messages.info(request, 'invalid credentials')
#     #         return redirect("teach")
#     # else:
#     #     return render (request, "teach-login.html")
