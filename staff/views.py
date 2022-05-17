from django.shortcuts import render

# Create your views here.
def staff(request, *args, **kwargs):
    return render(request, 'staff.html', {})