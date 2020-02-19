from django.contrib import admin

# Register your models here.
from user.models import *


# 用户
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'account', 'password', 'email', 'u_image')
    list_display = ('username', 'account', 'password', 'email', 'u_image')


# 视频
class VideoAdmin(admin.ModelAdmin):
    list_display = ('videoid', 'sectionname', 'time', 'courseid')
    list_editable = ('time',)


# 课程
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'intro', 'v_image', 'viewnum', 'likenum', 'collectnum', 'coursefile')
    readonly_fields = ('viewnum', 'likenum', 'collectnum')
    # list_display_links = ('coursefile',)
    list_filter = ('name',)
    fieldsets = (
        (None, {
            'fields': (
                'name', 'author', 'intro', 'v_image', 'viewnum', 'likenum', 'collectnum', 'coursefile', 'sumtime')
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('collegeid', 'classifyid')
        })
    )


# 大学
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'logo', 'co_image', 'schoolbadge')


class MaterialInline(admin.TabularInline):
    model = Material


class CourseInline(admin.TabularInline):
    model = Course


# 分类
class ClassifyAdmin(admin.ModelAdmin):
    inlines = [MaterialInline,CourseInline]
    list_display = ('name', 'intro')


# 资料
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'intro', 'downloadnum')


admin.site.register(User, UserAdmin)
admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Course, CourseAdmin)
