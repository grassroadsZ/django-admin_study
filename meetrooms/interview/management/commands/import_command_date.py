# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 15:22
# @Author  : grassroadsZ
# @File    : import_command_date.py
# 运行方式：python manage.py import_command_date --path file.csv

import csv
from django.core.management import BaseCommand
from interview.models import Candidate


# 类名必须为Command
class Command(BaseCommand):
    help = "从一个CSV文件中读取内容中候选人的列表,导入到数据库"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        path = options["path"]
        with open(path, "rt", encoding="utf-8") as f:
            # dialect指定文件，delimiter指定分隔符
            reader = csv.reader(f, dialect="excel", delimiter=',')
            for content in reader:
                Candidate.objects.create(username=content[0],
                                         city=content[1],
                                         phone=content[2],
                                         bachelor_school=content[3],
                                         major=content[4],
                                         degree=content[5],
                                         test_score_of_general_ability=content[6],
                                         paper_score=content[7])

