from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person


class PersonAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('graduated', 'major', 'company', 'job_title', 'about',)}),
    )


admin.site.register(Person, PersonAdmin)
