from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Person, User


class UserAdmin(BaseUserAdmin):
    model = User
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone_number',)}),
    )


class PersonAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
            (None, {'fields': ('graduated', 'major', 'company', 'job_title', 'about',)}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
