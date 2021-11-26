from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from . models import  User




UserAdmin.fieldsets+=(
    ('فیلد های اختصاصی',{'fields':('special_user',)}),
)


UserAdmin.list_display+=('is_special_user',)


admin.site.register(User,UserAdmin)
