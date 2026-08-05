from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from results.models import Result
from results.forms import ResultForm


@login_required
def result_management(request):

    search = request.GET.get("search", "")

    results = Result.objects.select_related(
        "student",
        "course"
    ).order_by("-id")

    if search:

        results = results.filter(

            Q(student__name__icontains=search) |

            Q(course__name__icontains=search) |

            Q(grade__icontains=search) |

            Q(result__icontains=search)

        )

    paginator = Paginator(
        results,
        10
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "result_management.html",
        {
            "results": page_obj,
            "page_obj": page_obj,
            "search": search,
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