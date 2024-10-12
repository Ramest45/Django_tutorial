from django.urls import path
from . import views as vf

urlpatterns = [
    path('feesdj/',vf.fees_django),
    path('feespy/',vf.fees_python),
]