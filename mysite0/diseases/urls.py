from django.urls import path
from . import views

urlpatterns = [
    path('',views.diseases_index),
    # path('all', views.all_diseases),
]