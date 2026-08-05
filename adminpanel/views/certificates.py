from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from certificates.models import Certificate


@login_required
def certificate_management(request):

    search = request.GET.get("search")

    certificates = Certificate.objects.all().order_by("-id")

    if search:

        certificates = certificates.filter(
            student__name__icontains=search
        )

    return render(
        request,
        "certificate_management.html",
        {
            "certificates": certificates,
            "search": search,
        }
    )


@login_required
def certificate_detail(request, certificate_id):

    certificate = get_object_or_404(
        Certificate,
        id=certificate_id
    )

    return render(
        request,
        "certificate_detail.html",
        {
            "certificate": certificate
        }
    )


@login_required
def delete_certificate(request, certificate_id):

    certificate = get_object_or_404(
        Certificate,
        id=certificate_id
    )

    certificate.delete()

    messages.success(
        request,
        "Certificate Deleted Successfully."
    )

    return redirect("certificate_management")