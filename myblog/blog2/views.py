# 要在template中显示内容，需要加的类,把内容响应给浏览器
from django.shortcuts import render

# 引入django的一个类
# from django.http import HttpResponse

# 在django的views中每一个请求都由一个函数来处理，需要创建一个函数
# def index(request):
# 因为要处理请求，需要先接收请求，在函数中添加一个参数，什么名称都是可以的，但有一个约定俗称叫request
# return HttpResponse("index.html")
# 返回回去,在里面传一个参数

# render(请求，页面，传替到前端的数据)
# 首页
def index(request):
    return render(request, 'blog2/index.html')

