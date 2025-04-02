from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'full_name', 'position', 'contact_number', 'created_at')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'position', 'contact_number')
    list_filter = ('position', 'created_at')
    readonly_fields = ('created_at', 'photo_preview')
    fieldsets = (
        ('Основная информация', {
            'fields': ('photo_preview', 'photo', 'full_name', 'position', 'bio', 'contact_number')
        }),
        ('Системная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def photo_preview(self, obj):
        """Отображение миниатюры фото в админке"""
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="50" style="border-radius: 5px;"/>'
        return "Нет фото"

    photo_preview.allow_tags = True
    photo_preview.short_description = "Превью"
