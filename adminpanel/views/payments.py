from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from payments.models import Payment
from payments.forms import PaymentForm


@login_required
def payment_management(request):

    search = request.GET.get("search")

    payments = Payment.objects.all().order_by("-id")

    if search:

        payments = payments.filter(
            student__name__icontains=search
        )

    return render(
        request,
        "payment_management.html",
        {
            "payments": payments,
            "search": search,
        }
    )


@login_required
def edit_payment(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id
    )

    if request.method == "POST":

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
                "Payment Updated Successfully."
            )

            return redirect("payment_management")

    else:

        form = PaymentForm(
            instance=payment
        )

    return render(
        request,
        "edit_payment.html",
        {
            "form": form
        }
    )


@login_required
def delete_payment(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id
    )

    payment.delete()

    messages.success(
        request,
        "Payment Deleted Successfully."
    )

    return redirect("payment_management")