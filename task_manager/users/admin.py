from django.contrib import admin

from .models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'created_at')
    search_fields = ['username', 'full_name', 'created_at']
# Register your models here.
