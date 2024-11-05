from django.urls import path

from . import views

urlpatterns = [
    path("", views.bienvenida, name="bienvenida"),
    path("details/<int:id>/", views.details, name="details"),
    path("contact/", views.contact, name = "contact"),
    #path("", views.index, name="index"),
]

