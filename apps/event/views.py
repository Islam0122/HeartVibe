from rest_framework import viewsets
from .models import Event , EventCategory
from .serializers import EventSerializer, EventCategorySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class CategoryEventViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    http_method_names = ['get', 'head', 'options']



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True).select_related('category')
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'category': ['exact'],
        'date': ['gte', 'lte', 'exact'],
        'is_active': ['exact'],
    }
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date']
    http_method_names = ['get', 'head', 'options']
