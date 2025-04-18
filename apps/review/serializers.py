from rest_framework import serializers
from .models import Review


class ReviewLangSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id','avatar','author', 'text', 'rating', 'created_at']


    def get_author(self, obj):
        lang = self.context.get('lang', 'ru')
        return getattr(obj, f'author_{lang}', obj.author)

    def get_text(self, obj):
        lang = self.context.get('lang', 'ru')
        return getattr(obj, f'text_{lang}', obj.text)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'rating', 'created_at', 'avatar')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating_display'] = f"{instance.rating} ⭐"
        return representation
