from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Placement
from .forms import PlacementForm


def placement_list(request):

    placements = Placement.objects.all().order_by(
        "-placement_date"
    )

    return render(
        request,
        "placement_list.html",
        {
            "placements": placements
        }
    )


def add_placement(request):

    if request.method == "POST":

        form = PlacementForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Placement Added Successfully."
            )

            return redirect(
                "placement_list"
            )

    else:

        form = PlacementForm()

    return render(
        request,
        "placement_form.html",
        {
            "form": form
        }
    )


def edit_placement(request, placement_id):

    placement = get_object_or_404(
        Placement,
        id=placement_id
    )

    if request.method == "POST":

        form = PlacementForm(
            request.POST,
            request.FILES,
            instance=placement
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Placement Updated Successfully."
            )

            return redirect(
                "placement_list"
            )

    else:

        form = PlacementForm(
            instance=placement
        )

    return render(
        request,
        "placement_form.html",
        {
            "form": form
        }
    )


def delete_placement(request, placement_id):

    placement = get_object_or_404(
        Placement,
        id=placement_id
    )

    placement.delete()

    messages.success(
        request,
        "Placement Deleted Successfully."
    )

    return redirect(
        "placement_list"
    )