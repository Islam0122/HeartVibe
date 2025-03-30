from rest_framework import viewsets
from .models import Event ,Category_Event
from .serializers import EventSerializer, EventListSerializer ,CategoryEventSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class CategoryEventViewSet(viewsets.ModelViewSet):
    queryset = Category_Event.objects.all()
    serializer_class = CategoryEventSerializer


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

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return super().get_serializer_class()