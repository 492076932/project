"""mysite0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from btoken import views as btoken_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index', views.index_view),
    # path('about', views.about_view),
    path('v1/users', user_views.UserView.as_view()),
    path('v1/users/', include('user.urls')),
    path('v1/tokens', btoken_views.TokensView.as_view()),
    path('user/',include('user.urls')),
    path('update/', include('update.urls')),
    path('diseases/', include('diseases.urls')),
    path('doctorsInfo/', include('doctor.urls')),
    #预约路由
    path('yuyue/',include('yuyue.urls')),

]
