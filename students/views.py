from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import StudentRegistrationForm, StudentProfileForm
from .models import Student


def register_student(request):

    if request.method == "POST":

        form = StudentRegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            student = form.save()

            User.objects.create_user(
                username=student.email,
                email=student.email,
                password=form.cleaned_data["password"]
            )

            messages.success(
                request,
                "Registration Successful! Please Login."
            )

            return redirect(
                "/students/login/"
            )

    else:

        form = StudentRegistrationForm()

    return render(
        request,
        "registration.html",
        {
            "form": form
        }
    )


def student_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            messages.success(
                request,
                "Login Successful!"
            )

            return redirect(
                "/dashboard/"
            )

        else:

            messages.error(
                request,
                "Invalid Email or Password"
            )

    return render(
        request,
        "login.html"
    )


@login_required(login_url="/students/login/")
def student_profile(request):

    student = Student.objects.filter(
        email=request.user.email
    ).first()

    if not student:

        messages.error(
            request,
            "Student profile not found."
        )

        return redirect(
            "/dashboard/"
        )

    return render(
        request,
        "student_profile.html",
        {
            "student": student
        }
    )


@login_required(login_url="/students/login/")
def edit_profile(request):

    student = Student.objects.filter(
        email=request.user.email
    ).first()

    if not student:

        messages.error(
            request,
            "Student profile not found."
        )

        return redirect(
            "/dashboard/"
        )

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile Updated Successfully!"
            )

            return redirect(
                "/students/profile/"
            )

    else:

        form = StudentProfileForm(
            instance=student
        )
        return render(
        request,
        "edit_profile.html",
        {
            "form": form
        }
    )


@login_required(login_url="/students/login/")
def student_logout(request):

    logout(request)

    messages.success(
        request,
        "Logout Successful!"
    )

    return redirect(
        "/students/login/"
    )


def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect(
                "/students/forgot-password/"
            )

        users = User.objects.filter(email=email)

        if not users.exists():

            messages.error(
                request,
                "Email not found."
            )

            return redirect(
                "/students/forgot-password/"
            )

        for user in users:

            user.set_password(new_password)
            user.save()

        messages.success(
            request,
            "Password changed successfully. Please login."
        )

        return redirect(
            "/students/login/"
        )

    return render(
        request,
        "forgot_password.html"
    )