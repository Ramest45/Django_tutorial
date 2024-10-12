from django.urls import path
from . import views

urlpatterns = [
    path('learnj/',views.learn_django),
    path('learnf',views.learn_python)
]