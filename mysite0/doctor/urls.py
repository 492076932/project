
from django.urls import path, include
from . import views
urlpatterns = [
    path('<int:id>/', views.list_view),
    path('<str:docname>/', views.doctor_view),

]
