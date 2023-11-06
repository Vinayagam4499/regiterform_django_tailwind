from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('new_register/', views.new_register, name='new_register'),
    
]