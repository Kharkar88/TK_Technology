from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Attendance
from .forms import AttendanceForm


@login_required
def attendance_management(request):

    attendance = Attendance.objects.select_related(
        "student"
    ).order_by("-date")

    return render(
        request,
        "attendance_management.html",
        {
            "attendance": attendance
        }
    )


@login_required
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance Added Successfully."
            )

            return redirect(
                "attendance_management"
            )

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance_form.html",
        {
            "form": form
        }
    )


@login_required
def edit_attendance(request, attendance_id):

    attendance = get_object_or_404(
        Attendance,
        id=attendance_id
    )

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance Updated Successfully."
            )

            return redirect(
                "attendance_management"
            )

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        "attendance_form.html",
        {
            "form": form
        }
    )


@login_required
def delete_attendance(request, attendance_id):

    attendance = get_object_or_404(
        Attendance,
        id=attendance_id
    )

    attendance.delete()

    messages.success(
        request,
        "Attendance Deleted Successfully."
    )

    return redirect(
        "attendance_management"
    )