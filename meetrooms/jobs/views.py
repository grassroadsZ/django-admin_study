from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.views import View
from .models import Job,  JOB_CITIES, JOB_TITLES,JOB_TYPES


def job_list(request):
    # 通过职位类型进行排序
    job_lists = Job.objects.order_by("job_type")
    # 加载模板文件
    template = loader.get_template("Job_list.html")

    # 定义上下文
    content = {"job_list": job_lists}

    # 把职位类型转换为字符串(原本为元祖)
    for job in job_lists:
        job.job_name = JOB_TITLES[job.job_name][1]
        job.city = JOB_CITIES[job.city][1]
        job.job_type = JOB_TYPES[job.job_type][1]
    return HttpResponse(template.render(content))
