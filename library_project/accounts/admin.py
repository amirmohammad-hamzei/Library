from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User,Otp

# Register your models here.

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'username', 'is_active', 'is_admin')
    search_fields = ('phone_number', 'username')
    ordering = ('created_at',)


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'code', 'created_at')
    search_fields = ('phone_number','code')
    ordering = ('created_at',)