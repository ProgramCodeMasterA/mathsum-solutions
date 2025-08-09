from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('problem', 'context', 'solved', 'created_on')
    search_fields = ['problem', 'created_on']
    list_filter = ('solved', 'created_on',)
    prepopulated_fields = {'context': ('problem',)}
    summernote_fields = ('context',)


# Register your models here.
admin.site.register(Comment)
