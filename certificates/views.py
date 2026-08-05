from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from students.models import Student
from payments.models import Payment
from .models import Certificate
import uuid


@login_required(login_url='/students/login/')
def certificate_dashboard(request):

    try:
        student = Student.objects.get(email=request.user.email)

        certificates = Certificate.objects.filter(student=student)

        payment = Payment.objects.filter(
            student=student,
            status='Paid'
        ).exists()

    except Student.DoesNotExist:

        student = None
        certificates = []
        payment = False

    context = {
        'student': student,
        'certificates': certificates,
        'payment': payment,
    }

    return render(
        request,
        'certificate_dashboard.html',
        context
    )


@login_required(login_url='/students/login/')
def generate_certificate(request):

    student = Student.objects.get(email=request.user.email)

    payment = Payment.objects.filter(
        student=student,
        status='Paid'
    ).exists()

    if not payment:

        messages.error(
            request,
            "Please complete your payment before generating the certificate."
        )

        return redirect('/certificates/')

    certificate = Certificate.objects.filter(
        student=student,
        course=student.course
    ).first()

    if certificate:

        messages.info(
            request,
            "Certificate already generated."
        )

    else:

        Certificate.objects.create(
            student=student,
            course=student.course,
            certificate_number=str(uuid.uuid4()).replace("-", "")[:12].upper()
        )

        messages.success(
            request,
            "Certificate generated successfully."
        )

    return redirect('/certificates/')


@login_required(login_url='/students/login/')
def view_certificate(request, certificate_id):

    certificate = get_object_or_404(
        Certificate,
        id=certificate_id
    )

    return render(
        request,
        'view_certificate.html',
        {
            'certificate': certificate
        }
    )