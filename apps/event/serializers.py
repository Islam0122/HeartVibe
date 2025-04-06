from rest_framework import serializers
from .models import Event, EventCategory
from django.utils.translation import get_language


class EventCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = EventCategory
        fields = ['id', 'name']

    def get_name(self, obj):
        lang = get_language()
        if lang == 'en' and obj.name_en:
            return obj.name_en
        elif lang == 'ky' and obj.name_ky:
            return obj.name_ky
        return obj.name


class EventSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    category = EventCategorySerializer()

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'date',
            'location', 'location_url',
            'category', 'is_active', 'image'
        ]

    def get_title(self, obj):
        lang = get_language()
        if lang == 'en' and obj.title_en:
            return obj.title_en
        elif lang == 'ky' and obj.title_ky:
            return obj.title_ky
        return obj.title

    def get_description(self, obj):
        lang = get_language()
        if lang == 'en' and obj.description_en:
            return obj.description_en
        elif lang == 'ky' and obj.description_ky:
            return obj.description_ky
        return obj.description