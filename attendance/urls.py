from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.attendance_management,
        name="attendance_management"
    ),

    path(
        "add/",
        views.add_attendance,
        name="add_attendance"
    ),

    path(
        "edit/<int:attendance_id>/",
        views.edit_attendance,
        name="edit_attendance"
    ),

    path(
        "delete/<int:attendance_id>/",
        views.delete_attendance,
        name="delete_attendance"
    ),

]