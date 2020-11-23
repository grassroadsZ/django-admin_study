# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 16:22
# @Author  : grassroadsZ
# @File    : urls.py
from django.conf.urls import url

from .views import job_list

urlpatterns = [
    url("^joblist/", job_list, name="joblist"),
]
