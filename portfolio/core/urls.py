from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('acerca-de-mí/', views.about, name="about"),
]
