from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)
class AccAdmin(UserAdmin):
    list_display=['username', 'Email','datejoined','is_admin','is_superuser','Department']
    search_fields= ['Email', 'username']
    readonly_fields= ['datejoined','password']

    filter_horizontal=()
    filter_vertical=()
    fieldsets=()


# Register your models here.

admin.site.register(Student, AccAdmin)
