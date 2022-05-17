from . import views

from django.urls import path

urlpatterns = [
    path('', views.account, name='account'),
    path('logout', views.logoutUser, name='logout'),
    path('base', views.base, name='base'),

    path('parent', views.parent, name='parent'),
    # path('teacher', views.teacher, name='teacher-registration'),
    # path('teacher-login', views.teacherlogin, name='teacher-login'),
    # path('teacher-dashboard', views.dashboard, name='teacher-dashboard'),
    # path('teach', views.teach, name='teach'),

]