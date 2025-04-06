from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from django.utils import translation

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
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


