
# from django.forms import ModelForm

from django import forms
from .models import User



class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


# class Teacherlogin(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = '__all__'

# class TeacherRegister(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = '__all__'