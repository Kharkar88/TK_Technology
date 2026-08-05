from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.certificate_dashboard,
        name='certificate_dashboard'
    ),

    path(
        'generate/',
        views.generate_certificate,
        name='generate_certificate'
    ),

    path(
        'view/<int:certificate_id>/',
        views.view_certificate,
        name='view_certificate'
    ),

]