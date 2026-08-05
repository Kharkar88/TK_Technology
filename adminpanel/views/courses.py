from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from courses.models import Course


@login_required
def course_management(request):

    search = request.GET.get("search", "")

    courses = Course.objects.all().order_by("-id")

    if search:

        courses = courses.filter(

            Q(name__icontains=search) |

            Q(category__icontains=search) |

            Q(duration__icontains=search)

        )

    paginator = Paginator(
        courses,
        10
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "course_management.html",
        {
            "courses": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


@login_required
def edit_course(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    if request.method == "POST":

        course.name = request.POST.get("name")

        course.category = request.POST.get("category")

        course.duration = request.POST.get("duration")

        course.fees = request.POST.get("fees")

        course.description = request.POST.get("description")

        course.save()

        messages.success(
            request,
            "Course Updated Successfully."
        )

        return redirect(
            "course_management"
        )

    return render(
        request,
        "edit_course.html",
        {
            "course": course
        }
    )


@login_required
def delete_course(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    course.delete()

    messages.success(
        request,
        "Course Deleted Successfully."
    )

    return redirect(
        "course_management"
    )