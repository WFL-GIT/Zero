"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from .views import MyView

urlpatterns = [
    path('World/',MyView.World,name='world'),
    path('index/',MyView.index,name='index'),
    path('login/',MyView.login,name='login'),
    path('index_unlog/',MyView.index_unlog,name='index_unlog'),
    path('logsuccess/',MyView.logsuccess,name='logsuccess'),
    path('register/',MyView.register,name='register'),
    path('forget/',MyView.forget_password,name='forget'),
    path('reset/',MyView.reset,name='reset'),

    #   默认进入主页
    re_path(r'^$',MyView.index)



]
