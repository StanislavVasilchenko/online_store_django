from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_content', 'date_of_creation', 'publication_sign', 'view_count')
    list_filter = ('publication_sign',)
