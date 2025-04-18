from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('avatar_display',
    'author', 'rating', 'created_at', 'author_en', 'author_ky', )
    list_filter = ('rating', 'created_at')
    search_fields = ('author', 'text')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {'fields': ('author', 'text', 'rating', 'avatar')}),
        ('Translations', {
            'fields': ('author_en', 'text_en', 'author_ky', 'text_ky'),
            'classes': ('collapse',),
        }),
        ('Additional Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ["created_at"]

    # Функция для отображения аватара в админке
    def avatar_display(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" width="100" height="100" style="object-fit: cover; border-radius: 50px;">')
        return "Нет изображения"

    avatar_display.allow_tags = True
    avatar_display.short_description = 'Аватар'


admin.site.register(Review, ReviewAdmin)
