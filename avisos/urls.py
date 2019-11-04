from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spain.jpg', views.spain, name='spain'),
]
