from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from students.models import Student
from .models import Feedback
from .forms import FeedbackForm


@login_required(login_url="/students/login/")
def add_feedback(request):

    try:

        student = Student.objects.get(
            email=request.user.email
        )

    except Student.DoesNotExist:

        messages.error(
            request,
            "Student not found."
        )

        return redirect("/dashboard/")

    if request.method == "POST":

        form = FeedbackForm(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)

            feedback.student = student
            feedback.course = student.course

            feedback.save()

            messages.success(
                request,
                "Thank you! Your feedback has been submitted successfully."
            )

            return redirect("/")

    else:

        form = FeedbackForm()

    return render(
        request,
        "feedback.html",
        {
            "form": form
        }
    )