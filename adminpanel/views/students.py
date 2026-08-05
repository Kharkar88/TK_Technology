from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from students.models import Student
from courses.models import Course


@login_required
def student_management(request):

    search = request.GET.get("search", "")

    students = Student.objects.select_related(
        "course"
    ).order_by("-id")

    if search:

        students = students.filter(

            Q(name__icontains=search) |

            Q(email__icontains=search) |

            Q(phone__icontains=search) |

            Q(course__name__icontains=search)

        )

    paginator = Paginator(
        students,
        10
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "student_management.html",
        {
            "students": page_obj,
            "page_obj": page_obj,
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