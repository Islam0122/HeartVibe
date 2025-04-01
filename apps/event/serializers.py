from rest_framework import serializers
from .models import EventCategory, Event

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name']


class EventSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer()
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'location_url', 'category', 'category_name', 'is_active', 'image']
