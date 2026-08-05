from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Course
from .forms import CourseForm


def course_list(request):

    courses = Course.objects.all()

    return render(
        request,
        "courses.html",
        {
            "courses": courses
        }
    )


def course_detail(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    return render(
        request,
        "course_detail.html",
        {
            "course": course
        }
    )


def add_course(request):

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course Added Successfully."
            )

            return redirect("course_management")
    else:

        form = CourseForm()

    return render(
        request,
        "add_course.html",
        {
            "form": form
        }
    )