from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from courses.models import Course
from instructors.models import Instructor
from students.models import Student
from contact.models import Contact
from payments.models import Payment
from certificates.models import Certificate
from feedback.models import Feedback
from placement.models import Placement


def home(request):

    courses = Course.objects.all()

    instructors = Instructor.objects.all()

    feedbacks = Feedback.objects.select_related(
        "student",
        "course"
    ).order_by("-id")[:6]

    placements = Placement.objects.all().order_by(
        "-placement_date"
    )[:6]

    return render(
        request,
        "index.html",
        {
            "courses": courses,
            "instructors": instructors,
            "feedbacks": feedbacks,
            "placements": placements,
        }
    )


@login_required(login_url="/students/login/")
def admin_dashboard(request):

    total_students = Student.objects.count()

    total_courses = Course.objects.count()

    total_instructors = Instructor.objects.count()

    total_contacts = Contact.objects.count()

    recent_students = Student.objects.order_by("-id")[:5]

    recent_placements = Placement.objects.order_by(
        "-placement_date"
    )[:5]

    student = None

    payment_status = "Pending"

    certificate_status = "Not Generated"

    progress = 25

    try:

        student = Student.objects.get(
            email=request.user.email
        )

        payment = Payment.objects.filter(
            student=student,
            status="Paid"
        ).exists()

        certificate = Certificate.objects.filter(
            student=student
        ).exists()

        if payment:

            payment_status = "Paid"

            progress = 70

        if certificate:

            certificate_status = "Generated"

            progress = 100

    except Student.DoesNotExist:

        student = None

    context = {

        "student": student,

        "payment_status": payment_status,

        "certificate_status": certificate_status,

        "progress": progress,

        "total_students": total_students,

        "total_courses": total_courses,

        "total_instructors": total_instructors,

        "total_contacts": total_contacts,

        "recent_students": recent_students,

        "recent_placements": recent_placements,

    }

    return render(
        request,
        "dashboard.html",
        context
    )