from django.shortcuts import render

### views for home page
def home_view(request):
    return render(request, 'home.html')

