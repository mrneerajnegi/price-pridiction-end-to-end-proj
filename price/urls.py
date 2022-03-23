from django.urls import path
from . import views

app_name="price"
urlpatterns=[
    path('',views.Home.as_view(),name="index"),
    path('item/<item>', views.InputPage.as_view(), name="item"),

]