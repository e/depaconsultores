from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "homes"
urlpatterns = [
    path("", views.index, name="index"),
    path("comprar/", views.sale, name="sale"),
    path("alquilar/", views.rent, name="rent"),
    path("compartir/", views.rooms, name="rooms"),
]