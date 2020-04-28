from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):

    list_display = ('title', 'date', 'location')
    list_filter = ('date', 'title', 'location')
    search_fields = ('title', 'location', 'description', 'qualifications', 'date')


admin.site.register(Job, JobAdmin)
