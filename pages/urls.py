from django.urls import path
from .import views

urlpatterns=[
    path('', views.mainpage),
    path('company/', views.company),
]