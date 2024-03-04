from django.contrib import admin
from .models import CustomUser


class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_superuser', 'is_teacher', 'is_student']


admin.site.register(CustomUser, CustomUserModelAdmin)
