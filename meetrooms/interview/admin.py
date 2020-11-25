from django.contrib import admin
from .models import Candidate


# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    exclude = ["creator", "created_date", "modified_date", "user_id"]
    list_display = ["username", "city", "bachelor_school", "first_score", "first_result", "first_interviewer",
                    "second_result", "second_interviewer", "hr_result", "last_editor"]

    # 定义搜索支持的字段
    search_fields = ["username", "phone", "email"]

    # 筛选条件
    list_filter = ["city", "first_result"]

    # 排序
    ordering = ["second_result", "first_result"]

    # 分组的写法：
    # fieldsets = [("分组的标题", {"fields": ("对应的字段1", "对应的字段2")})],
    # 字段不能是exclude里面的字段
    # 分组后的字段在一行显示时只需要将需要一行展示的字段放入一个元组中即可
    fieldsets = (("基础信息", {"fields": (
        "username", "city", "phone", ("email", "apply_position", "born_address"), "gender",
        "candidate_remark",
        ("bachelor_school", "master_school", "doctor_school"), "degree", "major", "test_score_of_general_ability",
        "paper_score", "last_editor")}),
                 ("第一次面试", {"fields": (
                     "first_score", "first_learning_ability", "first_professional_competency", "first_advantage",
                     "first_disadvantage", "first_result", "first_recommend_position", "first_interviewer",
                     "first_remark")}),
                 ("第二次面试", {"fields": (
                     "second_score", "second_learning_ability", "second_professional_competency",
                     "second_pursue_of_excellence", "second_communication_ability", "second_pressure_score",
                     "second_advantage", "second_disadvantage", "second_result", "second_recommend_position",
                     "second_interviewer", "second_remark")}),
                 ("HR面试", {"fields": (
                     ("hr_score", "hr_responsibility"), "hr_communication_ability", "hr_logic_ability", "hr_potential",
                     "hr_stability", "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer", "hr_remark",

                 )})
                 )


admin.site.register(Candidate, CandidateAdmin)
