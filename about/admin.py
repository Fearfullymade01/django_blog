from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.
    Uses Summernote for rich text editing of content.
    """
    summernote_fields = ('content',)
    list_display = ('title', 'updated_on')
