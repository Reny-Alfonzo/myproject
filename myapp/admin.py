from django.contrib import admin
from .models import TextContent, Comment

@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('content_type', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text_content', 'created_at', 'approved')
    search_fields = ('author', 'text')
    list_filter = ('approved', 'created_at')