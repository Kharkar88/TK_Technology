from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.payment_dashboard,
        name='payment_dashboard'
    ),

    path(
        'manage/',
        views.payment_list,
        name='payment_list'
    ),

    path(
        'add/',
        views.add_payment,
        name='add_payment'
    ),

    path(
        'edit/<int:payment_id>/',
        views.edit_payment,
        name='edit_payment'
    ),

    path(
        'delete/<int:payment_id>/',
        views.delete_payment,
        name='delete_payment'
    ),

]