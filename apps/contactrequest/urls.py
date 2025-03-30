from django.urls import path
from .views import ContactRequestCreateView

urlpatterns = [
    path('contact-requests/', ContactRequestCreateView.as_view(), name='contact-request-create'),
]