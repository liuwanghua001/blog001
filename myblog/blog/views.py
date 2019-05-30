# 要在template中显示内容，需要加的类,把内容响应给浏览器
from django.shortcuts import render
# Database note.txt
from . import models


def index(request):
    # 获取模型数据对象的实例,这里是查到数据库里面的
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


