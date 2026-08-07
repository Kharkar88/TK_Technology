from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from instructors.models import Instructor


@login_required
def trainer_management(request):

    search = request.GET.get("search")

    trainers = Instructor.objects.all().order_by("-id")

    if search:
        trainers = trainers.filter(
            name__icontains=search
        )

    return render(
        request,
        "trainer_management.html",
        {
            "trainers": trainers,
            "search": search,
        }
    )


@login_required
def add_trainer(request):

    if request.method == "POST":

        trainer = Instructor(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            experience=request.POST.get("experience"),
        )

        # Save uploaded image
        trainer.image = request.FILES.get("image")

        trainer.save()

        messages.success(
            request,
            "Trainer Added Successfully."
        )

        return redirect("trainer_management")


    return render(
        request,
        "add_trainer.html"
    )


@login_required
def edit_trainer(request, trainer_id):

    trainer = get_object_or_404(
        Instructor,
        id=trainer_id
    )

    if request.method == "POST":

        trainer.name = request.POST.get("name")
        trainer.email = request.POST.get("email")
        trainer.phone = request.POST.get("phone")
        trainer.subject = request.POST.get("subject")
        trainer.experience = request.POST.get("experience")

        # Update image if new image uploaded
        if request.FILES.get("image"):
            trainer.image = request.FILES.get("image")

        trainer.save()

        messages.success(
            request,
            "Trainer Updated Successfully."
        )

        return redirect("trainer_management")


    return render(
        request,
        "edit_trainer.html",
        {
            "trainer": trainer
        }
    )


@login_required
def delete_trainer(request, trainer_id):

    trainer = get_object_or_404(
        Instructor,
        id=trainer_id
    )

    trainer.delete()

    messages.success(
        request,
        "Trainer Deleted Successfully."
    )

    return redirect("trainer_management")