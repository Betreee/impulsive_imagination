from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'logged_in_home.html', {'user': user})
        else:
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


def register_request(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid() and form.password_check(form.cleaned_data['password1'])[0] == True:

            # save the form data to the database
            user = form.save()
            # log the user in
            login(request, user)
            # send a success message
            messages.success(request, 'Registration successful.')

            # Do something with the form data, then redirect to a success page
            return redirect('success')
        else:
            # If the form is not valid, re-render the form with the submitted data and validation errors
            form_password = form.password_check(form.cleaned_data['password1'])
            print(form_password)
            return render(request, 'users/register.html', {'form': form, 'form_password': form_password})
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
def success_view(request):
    return render(request,template_name= 'users/success.html')

def failed_view(request, form ):
    form = form
    print(form)
    return render(request,template_name= 'users/failed.html', context = {'form':form})

