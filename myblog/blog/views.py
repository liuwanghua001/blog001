# 要在template中显示内容，需要加的类,把内容响应给浏览器
from django.shortcuts import render
# Database note.txt
from . import models


def index(request):
    # 获取模型数据对象的实例,这里是查到数据库里面的
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

# 创建一个响应函数，创建一个文章页
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

# 文章添加页面
def edit_page(request):
    return render(request, 'blog/edit_page.html')

# 文章编辑页面
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})