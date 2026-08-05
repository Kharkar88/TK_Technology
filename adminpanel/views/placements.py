from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from placement.models import Placement
from placement.forms import PlacementForm


@login_required
def placement_management(request):

    search = request.GET.get("search", "")

    placements = Placement.objects.all().order_by("-id")

    if search:

        placements = placements.filter(

            Q(student_name__icontains=search) |

            Q(company_name__icontains=search) |

            Q(job_role__icontains=search)

        )

    paginator = Paginator(
        placements,
        10
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "placement_list.html",
        {
            "placements": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


@login_required
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
                "placement_management"
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


@login_required
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
                "placement_management"
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


@login_required
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
        "placement_management"
    )