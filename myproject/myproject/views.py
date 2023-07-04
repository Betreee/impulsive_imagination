from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

def user_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'users/profile.html', {'user': user})

### views for home page
def home_view(request):
    return render(request, 'home.html')

