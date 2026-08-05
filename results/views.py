from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Result
from .forms import ResultForm


@login_required
def result_management(request):

    results = Result.objects.select_related(
        "student",
        "course"
    ).order_by("-id")

    return render(
        request,
        "result_management.html",
        {
            "results": results
        }
    )


@login_required
def add_result(request):

    if request.method == "POST":

        form = ResultForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Result Added Successfully."
            )

            return redirect(
                "result_management"
            )

    else:

        form = ResultForm()

    return render(
        request,
        "result_form.html",
        {
            "form": form
        }
    )


@login_required
def edit_result(request, result_id):

    result = get_object_or_404(
        Result,
        id=result_id
    )

    if request.method == "POST":

        form = ResultForm(
            request.POST,
            instance=result
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Result Updated Successfully."
            )

            return redirect(
                "result_management"
            )

    else:

        form = ResultForm(
            instance=result
        )

    return render(
        request,
        "result_form.html",
        {
            "form": form
        }
    )


@login_required
def delete_result(request, result_id):

    result = get_object_or_404(
        Result,
        id=result_id
    )

    result.delete()

    messages.success(
        request,
        "Result Deleted Successfully."
    )

    return redirect(
        "result_management"
    )