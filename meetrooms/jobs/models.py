from django.contrib.auth.models import User
from django.db import models

# Create your models here.
JOB_TITLES = [
    (0, "开发工程师"),
    (1, "测试工程师"),
    (2, "产品经理")
]

JOB_TYPES = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类")
]
JOB_CITIES = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳")
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JOB_TYPES, verbose_name="职位类别")
    job_name = models.SmallIntegerField(blank=False, verbose_name="工作名称", choices=JOB_TITLES)
    city = models.SmallIntegerField(verbose_name="工作地点", choices=JOB_CITIES, blank=False)
    job_info = models.TextField(verbose_name="工作描述", blank=False, max_length=1024)
    job_requirement = models.TextField(verbose_name="职位要求", blank=False, max_length=1024)
    # creator没了的时候如何关联,用户删除时设置为Null，SET_NULL会报错
    creator = models.ForeignKey(User, verbose_name="创建人", on_delete=models.SET(None))
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        # 取列表中子元祖的第二个元素
        return JOB_TITLES[self.job_name][1]
