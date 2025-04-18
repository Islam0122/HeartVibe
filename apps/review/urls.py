from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet,ReviewView2Set
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'create-reviews', ReviewView2Set, basename='create-review')


urlpatterns = [
    path('', include(router.urls)),
]
