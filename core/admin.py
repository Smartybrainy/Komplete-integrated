from django.contrib import admin
from .models import IndexDesign
from embed_video.admin import AdminVideoMixin


@admin.register(IndexDesign)
class IndexDesignAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'timestamp',
    )

    search_fields = [
        'title',
        'content',
    ]

    list_per_page = 10