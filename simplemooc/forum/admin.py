from django.contrib import admin
from .models import Thread, Reply


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'modified']
    search_fields = ['title', 'author__email', 'body']
    prepopulated_fields = {'slug': ('title',)}


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['thread', 'author', 'correct', 'created', 'modified']
    search_fields = ['thread__title', 'author__email', 'reply']


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply, ReplyAdmin)