from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'updated']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)