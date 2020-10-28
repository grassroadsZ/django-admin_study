from django.contrib.auth.models import User
from django.db import models

# Create your models here.
JOB_TITLES = [
    (0, "开发"),
    (1, "测试"),
    (2, "产品")
]

JOB_CITIES = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳")
]


class Job(models.Model):
    job_name = models.SmallIntegerField(verbose_name="工作名称", choices=JOB_TITLES)
    city = models.SmallIntegerField(verbose_name="工作地点", choices=JOB_CITIES)
    job_info = models.TextField(verbose_name="工作信息", blank=False, max_length=1024)
    # todo:考虑当owner没了的时候如何关联
    owner = models.ForeignKey(User,)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
