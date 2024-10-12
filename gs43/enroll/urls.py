from django.urls import path
from . import views,include

urlpatterns = [
    path('student/',views.showformate),
    path('reg/',include('enroll.urls')),
]
