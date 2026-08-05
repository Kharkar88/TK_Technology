from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from students.models import Student
from courses.models import Course
from instructors.models import Instructor
from payments.models import Payment
from certificates.models import Certificate
from placement.models import Placement
from attendance.models import Attendance
from results.models import Result
from feedback.models import Feedback


@login_required
def admin_dashboard(request):

    recent_students = Student.objects.order_by("-id")[:5]

    recent_placements = Placement.objects.order_by("-id")[:5]

    recent_results = Result.objects.select_related(
        "student",
        "course"
    ).order_by("-id")[:5]

    context = {

        "student_count": Student.objects.count(),

        "course_count": Course.objects.count(),

        "trainer_count": Instructor.objects.count(),

        "payment_count": Payment.objects.count(),

        "certificate_count": Certificate.objects.count(),

        "placement_count": Placement.objects.count(),

        "attendance_count": Attendance.objects.count(),

        "result_count": Result.objects.count(),

        "feedback_count": Feedback.objects.count(),

        "recent_students": recent_students,

        "recent_placements": recent_placements,

        "recent_results": recent_results,

    }

    return render(
        request,
        "admin_dashboard.html",
        context
    )