
from django.urls import re_path
from . import views
app_name = 'blog'
urlpatterns = [

    # blog2.urls 需要有urls这样一个文件urls.py
    # （路径名称，指向哪里）
    re_path('^index/$', views.index),
    re_path('^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path('^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    re_path('^edit/action$', views.edit_action, name='edit_action')
    ]