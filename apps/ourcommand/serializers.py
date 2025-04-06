from rest_framework import serializers
from .models import TeamMember
from django.utils import translation

class TeamMemberSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = ['photo', 'full_name', 'position', 'bio', 'contact_number', 'created_at', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None

    def get_full_name(self, obj):
        lang = translation.get_language() or 'ru'
        return getattr(obj, f"full_name_{lang}", obj.full_name)

    def get_position(self, obj):
        lang = translation.get_language() or 'ru'
        return getattr(obj, f"position_{lang}", obj.position)

    def get_bio(self, obj):
        lang = translation.get_language() or 'ru'
        return getattr(obj, f"bio_{lang}", obj.bio)
