from django.urls import path

from . import views

app_name = "workshops"

urlpatterns = [
    path("", views.workshop_list, name="list"),
    path("workshops/<int:pk>/", views.workshop_detail, name="detail"),
    path("workshops/<int:pk>/register", views.workshop_register, name="register"),
    path(
        "registration/success", views.registration_success, name="registration_success"
    ),
]
