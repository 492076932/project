from django.urls import path, re_path
from . import views
urlpatterns=[
    # path('home',views.home_view),
    path('home', views.home_view.as_view()),
    path('yuyue',views.yuyue)
]