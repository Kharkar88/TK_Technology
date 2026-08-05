from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from students.models import Student
from .models import Payment
from .forms import PaymentForm


@login_required(login_url='/students/login/')
def payment_dashboard(request):

    try:
        student = Student.objects.get(email=request.user.username)
        payments = Payment.objects.filter(student=student)

    except Student.DoesNotExist:
        student = None
        payments = []

    return render(
        request,
        'payment_dashboard.html',
        {
            'student': student,
            'payments': payments,
        }
    )


@login_required(login_url='/admin/')
def payment_list(request):

    payments = Payment.objects.all().order_by('-id')

    return render(
        request,
        'payment_list.html',
        {
            'payments': payments
        }
    )


@login_required(login_url='/admin/')
def add_payment(request):

    if request.method == 'POST':

        form = PaymentForm(request.POST)

        if form.is_valid():

            payment = form.save(commit=False)
            payment.course = payment.student.course
            payment.save()

            messages.success(
                request,
                'Payment Added Successfully.'
            )

            return redirect('payment_list')

    else:

        form = PaymentForm()

    return render(
        request,
        'payment_form.html',
        {
            'form': form
        }
    )


@login_required(login_url='/admin/')
def edit_payment(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id
    )

    if request.method == 'POST':

        form = PaymentForm(
            request.POST,
            instance=payment
        )

        if form.is_valid():

            payment = form.save(commit=False)
            payment.course = payment.student.course
            payment.save()

            messages.success(
                request,
                'Payment Updated Successfully.'
            )

            return redirect('payment_list')

    else:

        form = PaymentForm(
            instance=payment
        )

    return render(
        request,
        'payment_form.html',
        {
            'form': form
        }
    )


@login_required(login_url='/admin/')
def delete_payment(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id
    )

    payment.delete()

    messages.success(
        request,
        'Payment Deleted Successfully.'
    )

    return redirect('payment_list')