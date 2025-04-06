from rest_framework import serializers
from .models import News
from django.utils import translation


class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'image', 'image_url', 'created_at', 'updated_at')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_title(self, obj):
        lang = translation.get_language() or 'ru'
        return getattr(obj, f"title_{lang}", obj.title)

    def get_content(self, obj):
        lang = translation.get_language() or 'ru'
        return getattr(obj, f"content_{lang}", obj.content)
