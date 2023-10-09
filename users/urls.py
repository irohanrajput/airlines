from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_users, name="index_users"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("flight_redr/", views.flight_redr_view, name="flight_redr"),
]
