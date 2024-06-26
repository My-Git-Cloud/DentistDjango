from . import views
from django.urls import path


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("appointment/", views.appointment, name="appointment"),
    path("book_appointment/", views.book_appointment, name="book_appointment"),
]
