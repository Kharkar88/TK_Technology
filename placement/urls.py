from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.placement_list,
        name="placement_list"
    ),

    path(
        "add/",
        views.add_placement,
        name="add_placement"
    ),

    path(
        "edit/<int:placement_id>/",
        views.edit_placement,
        name="edit_placement"
    ),

    path(
        "delete/<int:placement_id>/",
        views.delete_placement,
        name="delete_placement"
    ),

]