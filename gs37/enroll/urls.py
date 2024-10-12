from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.showformate),
    path('thanks/',views.thankyou),
]
