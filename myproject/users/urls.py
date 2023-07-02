from django.urls import path
from .views import register_request, success_view, failed_view, login_view
urlpatterns = [
    path("register/", register_request, name="register"),
    path("success/", success_view, name="success"),
    path("failed/", failed_view, name="failed"),
    path("login/", login_view , name="login"),
]