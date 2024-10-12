from django.urls import path,register_converter
from enroll import views,converters

register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('session/<yyyy:year>/',views.show_details,name="detail"),

]
# by default dynamic url me string type jata hai
