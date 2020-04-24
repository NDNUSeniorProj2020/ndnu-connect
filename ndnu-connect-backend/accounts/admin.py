from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AddUserForm, UpdateUserForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # Define forms and model
    form = UpdateUserForm
    add_form = AddUserForm
    model = User

    # Setup admin view table
    search_fields = ('email', 'first_name',
                     'last_name', 'phone_number',)
    list_filter = ('is_staff', 'is_active',)
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name',
                    'phone_number', 'is_active', 'is_staff',)

    # Specify field sets
    fieldsets = (
        (None, {
            'fields': ('email', 'password')}),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Alumni Information', {
            'fields': ('graduated', 'year_graduated', 'major', 'company', 'job_title', 'about',)}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)})
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name', 'phone_number', 'password1',
                    'password2'
                )
            }
        ),
    )


admin.site.register(User, UserAdmin)
