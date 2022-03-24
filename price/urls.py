from django.urls import path
from . import views

app_name="price"
urlpatterns=[
    path('',views.Home.as_view(),name="index"),
    path('car/', views.Car.as_view(),name="car"),
    path('bike/', views.Bike.as_view(),name="bike"),
    path('house/', views.House.as_view(),name="house"),

]