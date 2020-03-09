from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AddUserForm, UpdateUserForm
from .models import Person, User


class UserAdmin(BaseUserAdmin):
    # Define forms and model
    form = UpdateUserForm
    add_form = AddUserForm
    model = User

    # Setup admin view table
    search_fields = ('email', 'first_name', 'last_name', 'phone_number',)
    list_filter = ('is_staff', 'is_active',)
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff',)

    # Specify feild sets
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name', 'password1',
                    'password2'
                )
            }
        ),
    )


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('graduated', 'major', 'company', 'job_title', 'about', 'user')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
