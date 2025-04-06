from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    save_on_top = True


    def image_preview(self, obj):
        """Отображает миниатюру изображения в админке"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="60" style="object-fit: cover;" />')
        return "Нет изображения"

    image_preview.short_description = "Превью"

