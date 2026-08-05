from django.urls import path
from . import views

urlpatterns = [

    path(
        'register/',
        views.register_student,
        name='register_student'
    ),

    path(
        'login/',
        views.student_login,
        name='student_login'
    ),

    path(
        'logout/',
        views.student_logout,
        name='student_logout'
    ),

    path(
        'profile/',
        views.student_profile,
        name='student_profile'
    ),

    path(
        'edit-profile/',
        views.edit_profile,
        name='edit_profile'
    ),

    path(
        'forgot-password/',
        views.forgot_password,
        name='forgot_password'
    ),

]