from django.shortcuts import render

# Create your views here.
def student(request, *args, **kwargs):
    return render(request, 'student.html', {})