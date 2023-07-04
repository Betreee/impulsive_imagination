from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("register/", register_request, name="register"),
    path("success/", success_view, name="success"),
    path("failed/", failed_view, name="failed"),
    path("profile/", profile_view, name="profile"),
    path("login/", LoginView.as_view(next_page="login"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
 path('profile/<int:user_id>/', user_profile_view, name='user_profile'),
 path('update/', views.update_profile, name='update_profile'),
]
