from django.urls import path
from . import views

urlpatterns = [
    path('contactamé/', views.contact, name="contact"), 
]
