from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_phone', 'status_badge', 'created_at')
    list_display_links = ('name', 'formatted_phone')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone_number')
    list_per_page = 20
    date_hierarchy = 'created_at'
    fieldsets = (
        (_('Контактная информация'), {
            'fields': ('name', 'phone_number')
        }),
        (_('Статус'), {
            'fields': ('is_processed', 'created_at','updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at','updated_at')
    def formatted_phone(self, obj):
        return format_html(
            '<a href="tel:{0}" style="white-space: nowrap;">'
            '<i class="fas fa-phone-alt"></i> {0}</a>',
            obj.phone_number
        )

    formatted_phone.short_description = _('Телефон')

    def status_badge(self, obj):
        color, text, icon = ('green', _('Обработано'), 'check-circle') if obj.is_processed \
            else ('orange', _('В ожидании'), 'hourglass-half')
        return format_html(
            '<span style="color: {}; background: #f5f5f5; padding: 3px 8px; border-radius: 4px;">'
            '<i class="fas fa-{}"></i> {}</span>',
            color, icon, text
        )

    status_badge.short_description = _('Статус')

    # CSS/JS для админки
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',)
        }