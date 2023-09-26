from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    # here, we're puttin "localhost/flights/n" as url from where it gets the flight_id = n, where n is an integer obv.
    path("<int:flight_id>/book", views.book, name="book"),

]
