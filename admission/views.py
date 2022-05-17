from django.shortcuts import render

# Create your views here.
def admission(request, *args, **kwargs):
    return render(request, "admission.html", {})