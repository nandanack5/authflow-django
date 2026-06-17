from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, UpdateProfileForm


def home(request):
    return render(request, "accounts/home.html")


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully! Please login."
            )

            return redirect("/login/")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.username}!"
            )

            return redirect("/dashboard/")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "accounts/login.html")


@login_required(login_url="/login/")
def dashboard(request):

    return render(
        request,
        "accounts/dashboard.html"
    )

@login_required(login_url="/login/")
def profile(request):

    return render(
        request,
        "accounts/profile.html"
    )

@login_required(login_url="/login/")
def edit_profile(request):

    if request.method == "POST":

        form = UpdateProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully!"
            )

            return redirect("/profile/")

    else:

        form = UpdateProfileForm(
            instance=request.user
        )

    return render(

        request,

        "accounts/edit_profile.html",

        {

            "form": form

        }

    )


def logout_user(request):

    logout(request)

    messages.info(
        request,
        "You have been logged out."
    )

    return redirect("/")

@login_required(login_url="/login/")
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully!"
            )

            return redirect("/profile/")

    else:

        form = PasswordChangeForm(request.user)

    return render(

        request,

        "accounts/change_password.html",

        {

            "form": form

        }

    )