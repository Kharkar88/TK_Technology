from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from contact.models import Contact


@login_required
def contact_management(request):

    search = request.GET.get("search")

    contacts = Contact.objects.all().order_by("-id")

    if search:

        contacts = contacts.filter(
            name__icontains=search
        )

    return render(
        request,
        "contact_management.html",
        {
            "contacts": contacts,
            "search": search,
        }
    )


@login_required
def contact_detail(request, contact_id):

    contact = get_object_or_404(
        Contact,
        id=contact_id
    )

    return render(
        request,
        "contact_detail.html",
        {
            "contact": contact
        }
    )


@login_required
def delete_contact(request, contact_id):

    contact = get_object_or_404(
        Contact,
        id=contact_id
    )

    contact.delete()

    messages.success(
        request,
        "Contact Deleted Successfully."
    )

    return redirect("contact_management")