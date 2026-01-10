from django.contrib import admin

from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("author", "body", "approved")
    readonly_fields = ()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    search_fields = ("title", "content", "author__username")
    list_filter = ("status", "author", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "approved", "created_on")
    search_fields = ("author__username", "body", "post__title")
    list_filter = ("approved", "created_on")
    actions = ("mark_approved", "mark_unapproved")

    def mark_approved(self, request, queryset):
        queryset.update(approved=True)
    mark_approved.short_description = "Mark selected comments as approved"

    def mark_unapproved(self, request, queryset):
        queryset.update(approved=False)
    mark_unapproved.short_description = "Mark selected comments as unapproved"
