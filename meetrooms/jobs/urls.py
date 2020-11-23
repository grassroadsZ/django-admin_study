# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 16:22
# @Author  : grassroadsZ
# @File    : urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url("^joblist/", views.job_list, name="joblist"),
    url("^job/(?P<job_id>\d+)/$", views.detail, name="detail"),
]
