from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'full_name', 'position', 'contact_number', 'created_at')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'position', 'contact_number')
    list_filter = ('position', 'created_at')
    readonly_fields = ('created_at', 'photo_preview')

    def photo_preview(self, obj):
        """Отображение миниатюры фото в админке"""
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="100" style="object-fit: cover; border-radius: 50px;">')
        return "Нет изображения"

    photo_preview.allow_tags = True
    photo_preview.short_description = "Превью"
