from django.shortcuts import render

# Create your views here.
def about(request, *args, **kwargs):
    return render(request, "about.html", {})
def detail(request, *args, **kwargs):
    return render(request, "detail.html", {})    