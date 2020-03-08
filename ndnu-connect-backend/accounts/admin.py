from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Person, User


class UserAdmin(BaseUserAdmin):
    model = User
    list_filter = ('is_staff', 'is_active',)
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff',)})
    )


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {'fields': ('graduated', 'major', 'company', 'job_title', 'about',)}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
