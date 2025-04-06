from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .models import Event, EventCategory
from .serializers import EventSerializer, EventCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import translation


class CategoryEventViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    http_method_names = ['get', 'head', 'options']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang')
        if lang:
            translation.activate(lang)
        return context


def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.request.query_params.get('lang')
    if lang:
        translation.activate(lang)
    serializer = self.get_serializer(instance)
    return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True).select_related('category')
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'category': ['exact'],
        'date': ['gte', 'lte', 'exact'],
        'is_active': ['exact'],
    }
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date']
    http_method_names = ['get', 'head', 'options']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang')
        if lang:
            translation.activate(lang)
        return context

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.request.query_params.get('lang')
        if lang:
            translation.activate(lang)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
