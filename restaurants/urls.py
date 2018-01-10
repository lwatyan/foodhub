from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
   path('list/', views.restaurant_list, name="list"),
   path('detail/<int:restaurant_id>/', views.restaurant_detail, name="detail"), 
]

