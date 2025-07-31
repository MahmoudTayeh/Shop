from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('name', 'phone_number', 'email', 'address', 'is_manager','created_at')
    search_fields = ('name', 'email','phone_number',)
    #  list_editable = ('phone_number', 'email', 'address', 'is_manager',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('phone_number', 'address', 'is_manager', 'created_at')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('phone_number','email', 'address', 'is_manager')
        }),
    )
admin.site.register(CustomUser,CustomUserAdmin)