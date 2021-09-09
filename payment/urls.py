from django.urls import path 
from .views import *



urlpatterns = [
   path("donate", home, name="home"),
   path("", index, name="index"),
   path("success", success, name="success"),
]