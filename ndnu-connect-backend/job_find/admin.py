from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):

    list_display = ('title', 'date')
    list_filter =('date', 'title')
    search_fields = ('title', 'description', 'qualifications', 'date' )

admin.site.register(Job, JobAdmin)
admin.site.site_header = "Job" #title
