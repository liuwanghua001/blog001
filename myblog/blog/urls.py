
from django.urls import path
from . import views

urlpatterns = [

    # blog2.urls 需要有urls这样一个文件urls.py
    # 一般是修改这个下在贩url path("修改第一个参数")
    path('index/', views.index)
    ]