from django.urls import path
from . import views as vc

urlpatterns = [
    path('learndj/',vc.learn_django),
    path('learnpy/',vc.learn_python),
]