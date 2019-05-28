from django.db import models

# Create your models here.

class Article (models.Model):
    title = models.CharField(max_length=32, default="titles")
    content = models.TextField(null=True)

# 生成数据表
# manage.py同级目录
# 执行生成 python manage.py makemigration app名（可选）
# 再执行迁移 python manage.py migrate
# 查看表字段信息（熟习的字段展示）： python manage.py sqlmigrate blog 0001

# 后台添加的文章默认生成的对象变成自己的文章标题
#  这里代码缩进有要求
    def __str__(self):
        return self.title

