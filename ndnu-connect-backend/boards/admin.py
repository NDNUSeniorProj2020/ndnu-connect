from django.contrib import admin
from .models import Board, Topic, Post


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'last_updated')
    list_filter = ('last_updated', 'subject')


class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'topic', 'created_by')
    list_filter = ('topic', 'updated_at')
    

admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
