from django.contrib import admin

# Register your models here.
from .models import Company, City, Vacancy, Skill, Salary, Schedule,\
    Experience, Employment, Param


admin.site.register(Company)
admin.site.register(City)
admin.site.register(Vacancy)
admin.site.register(Skill)
admin.site.register(Salary)
admin.site.register(Schedule)
admin.site.register(Experience)
admin.site.register(Employment)


def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


set_active.short_description = "Активировать"


def set_de_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


set_de_active.short_description = "Деактивировать"


class ParamAdmin(admin.ModelAdmin):
    list_display = ['key_words', 'author', 'is_active']
    actions = [set_active, set_de_active]


admin.site.register(Param, ParamAdmin)

