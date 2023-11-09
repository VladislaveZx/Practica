from django.contrib import admin

# Register your models here.
from .models import User, Stud, Requests, StudGraph

class UserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'full_name']

class StudAdmin(admin.ModelAdmin):
    list_display = ['id', 'studnum', 'studname', 'studgroup', 'studyear']

class RequestsAdmin(admin.ModelAdmin):
    list_display = ['user', 'studnum', 'date', 'destination', 'status']

class StudGraphAdmin(admin.ModelAdmin):
    list_display = ['studcourse', 'studgroup', 'week', 'day', 'time_start', 'time_end', 'lesson', 'lesson_type', 'teacher']

admin.site.register(User, UserAdmin)
admin.site.register(Stud, StudAdmin)
admin.site.register(Requests, RequestsAdmin)
admin.site.register(StudGraph, StudGraphAdmin)

