from django.contrib import admin
from .models import Numbers , User


class AdminNumber(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'mobile']


class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']


admin.site.register(User, AdminUser)
admin.site.register(Numbers, AdminNumber)
