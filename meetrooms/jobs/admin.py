from django.contrib import admin
from .models import Job


# Register your models here.


class JobAdmin(admin.ModelAdmin):
    # 列表页展示字段
    list_display = ["job_name", "job_type", "city", "creator", "create_time"]

    # 定义后台列表页中不显示的字段
    exclude = ["creator"]

    # 保存模型类对象之前进行的操作
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

# 注册model类
admin.site.register(Job, JobAdmin)
