from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from students.models import Student
from courses.models import Course
from instructors.models import Instructor
from payments.models import Payment
from certificates.models import Certificate


@login_required
def admin_dashboard(request):

    context = {

        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'trainer_count': Instructor.objects.count(),
        'payment_count': Payment.objects.count(),
        'certificate_count': Certificate.objects.count(),

    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )


# ---------------- STUDENTS ---------------- #

@login_required
def student_management(request):

    search = request.GET.get("search", "")

    students = Student.objects.all().order_by("-id")

    if search:

        students = students.filter(
            name__icontains=search
        ) | Student.objects.filter(
            email__icontains=search
        ) | Student.objects.filter(
            phone__icontains=search
        )

        students = students.distinct()

    return render(
        request,
        "student_management.html",
        {
            "students": students,
            "search": search,
        }
    )


@login_required
def edit_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.course_id = request.POST.get("course")

        student.save()

        messages.success(
            request,
            "Student Updated Successfully."
        )

        return redirect(
            "student_management"
        )

    courses = Course.objects.all()

    return render(
        request,
        "edit_student.html",
        {
            "student": student,
            "courses": courses,
        },
    )


@login_required
def delete_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    student.delete()

    messages.success(
        request,
        "Student Deleted Successfully."
    )

    return redirect(
        "student_management"
    )


# ---------------- COURSES ---------------- #

@login_required
def course_management(request):

    courses = Course.objects.all().order_by('-id')

    return render(
        request,
        'course_management.html',
        {
            'courses': courses
        }
    )