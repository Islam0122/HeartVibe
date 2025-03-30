from rest_framework import serializers
from .models import ContactRequest

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['name', 'phone_number', 'is_processed', 'created_at','updated_at']
        read_only_fields = ['is_processed', 'created_at','updated_at']