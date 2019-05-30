"""myblog URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog2/', include('blog2.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
# jjlfjs
urlpatterns = [
    # 这里每一个url都是一个函数，每个函数都有很多种配置方式
    # 参数1：url的址 参数2：一个池
    re_path('admin/', admin.site.urls),
    # blog2.urls 需要有urls这样一个文件urls.py
    # blog2/这个是根位置，后面可以
    re_path('blog/', include('blog.urls', namespace='blog')),
    re_path('blog2/', include('blog2.urls')),

]
