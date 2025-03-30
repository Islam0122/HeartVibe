# views.py
import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContactRequest
from .serializers import ContactRequestSerializer

TELEGRAM_BOT_TOKEN = '7928285404:AAFPDogQ1zHS6H7b9dGUmZir0bKHM91U5Ok'
TELEGRAM_CHAT_ID = '-4778860820'


class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_to_telegram(instance)

    def send_to_telegram(self, contact):
        message = (
            f"📞 Новая заявка!\n"
            f"Имя: {contact.name}\n"
            f"Телефон: {contact.phone_number}\n"
            f"Дата: {contact.created_at.strftime('%d.%m.%Y %H:%M')}"
        )
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        try:
            requests.post(url, data=payload)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка отправки в Telegram: {e}")