from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'image', 'image_url', 'created_at', 'updated_at')

    def get_image_url(self, obj):
        """Возвращает полный URL изображения"""
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

