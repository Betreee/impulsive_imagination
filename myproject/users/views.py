from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


# def login(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         render(request, "users/profile.html")
#     else:
#         return redirect("login")


def profile_view(request):
    print("this is profile view ", request.user.is_authenticated)
    print(request.user)
    if request.user.is_authenticated:
        if UserProfile.objects.filter(user=request.user).exists() == False:
            UserProfile.create_user_profile(
                sender=request.user, instance=request.user, created=True
            )
        profile = UserProfile.objects.get(user=request.user)
        user = request.user

        if request.method == "POST":
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect("profile")
        form = UserProfileForm(instance=profile)
        context = {"profile": profile, "user": user, "form": form}
        print("this is user ", user)
        print("this is profile ", profile)

        return render(request, "profile.html", context)

    return render(request, "users/profile.html")


def login_request(request):
    print("this is login request ", request.user.is_authenticated)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print("user is not none")
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "users/profile.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="users/login.html", context={"form": form}
    )


def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            # log the user in
            authenticate(request, username=user.username, password=user.password)
            login(request, user)
            # send a success message
            messages.success(request, "Registration successful.")

            # Do something with the form data, then redirect to a success page
            return redirect("success")
        else:
            # If the form is not valid, re-render the form with the submitted data and validation errors

            return render(
                request,
                "users/register.html",
                {"form": form},
            )
    else:
        form = RegistrationForm()
        return render(request, "users/register.html", {"form": form})


def success_view(request):
    return render(request, template_name="users/success.html")


def failed_view(request, form):
    form = form
    print(form)
    return render(request, template_name="users/failed.html", context={"form": form})


from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
def user_profile_view(request, user_id):
    print("this is user profile view ", request.user.is_authenticated)
    user = request.user
    profile = UserProfile.objects.get(user=user_id)
    form = UserProfileForm(instance=profile)
    print("this is user profile view ", profile)
    if request.user.is_authenticated and  not UserProfile.objects.filter(user=user).exists():
        print("this is user profile view ", request.user.is_authenticated)
        if not UserProfile.objects.filter(user=user).exists():
            UserProfile.create_user_profile(sender=user, instance=user, created=True)
       
        profile = UserProfile.objects.get(user=user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            UserProfile.save()
            return redirect("profile")
    return render(
        request,
        "profile.html",
        context={
            "profile": profile,
            "user": user,
            "form": form,
        },
    )

def update_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            pro = UserProfile.objects.get(user=request.user)
            print(pro)
            form.update()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "profile.html", {"form": form})