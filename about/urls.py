from . import views

from django.urls import path

urlpatterns = [
    path('', views.about, name='about'),
    path('about-school', views.detail, name='about'),

]
