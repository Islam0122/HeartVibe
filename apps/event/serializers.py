from rest_framework import serializers
from .models import Event, Category_Event


class CategoryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Event
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    # Сериализатор для изображения (возвращает полный URL)
    image = serializers.SerializerMethodField()
    # Вложенный сериализатор для категории
    category = CategoryEventSerializer(read_only=True)
    # ID категории для записи (write-only поле)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category_Event.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'location',
            'location_url',
            'image',
            'category',
            'category_id',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None


class EventListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'location', 'category_name', 'image_thumbnail']

    def get_image_thumbnail(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None