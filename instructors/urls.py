from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_instructor, name='add_instructor'),
]