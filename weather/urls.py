from django.urls import path

from weather import views

urlpatterns = [
    path("<str:location>/", views.weather, name="weather"),
]
