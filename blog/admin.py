from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    actions = ['make_published', 'make_draft']


    def make_published(self, request, queryset):
        updated = queryset.update(status='published')
        if updated == 1:
            message_bit = '1 post was'
        else:
            message_bit = '%s posts were' %updated
        self.message_user(request, '%s successfully updated.' %message_bit)
    make_published.short_description = 'Update to Published'

    def make_draft(self, request, queryset):
        updated = queryset.update(status='draft')
        if updated == 1:
            message_bit = '1 post was'
        else:
            message_bit = '%s posts were' %updated
        self.message_user(request, '%s successfully updated.' %message_bit)
    make_draft.short_description = 'Update to draft'