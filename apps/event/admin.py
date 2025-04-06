from django.contrib import admin
from django.utils.html import format_html
from .models import Event, EventCategory


@admin.register(EventCategory)
class CategoryEventAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'date', 'location', 'category', 'is_active')
    list_filter = ('category', 'is_active', 'date')
    search_fields = ('title', 'description', 'location')
    list_editable = ('is_active',)
    readonly_fields = ('display_image','created_at', 'updated_at')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 5px;" />', obj.image.url)
        return "—"

    display_image.short_description = "Превью"