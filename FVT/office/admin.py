from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name']
    list_editable = ['full_name']
    list_display_links = ['username']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['studnum', 'studname', 'studgroup', 'studyear']
    list_editable = ['studname', 'studgroup', 'studyear']
    list_display_links = ['studnum']


class RequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'studnum', 'date', 'organisation', 'created']
    list_editable = ['created']


admin.site.register(models.Users, UserAdmin)
admin.site.register(models.Students, StudentAdmin)
admin.site.register(models.Requests, RequestAdmin)
