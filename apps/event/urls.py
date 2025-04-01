from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CategoryEventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'events-categories', CategoryEventViewSet, basename='category')

urlpatterns = router.urls