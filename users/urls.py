from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, dashboard
from .views import home, register, dashboard, delete_task
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),

    path(
        "login/",
        LoginView.as_view(template_name="login.html"),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(next_page="login"),
        name="logout"
    ),

    path(
        "delete/<int:task_id>/",
        delete_task,
        name="delete_task"
    ),

    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset.html"
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]