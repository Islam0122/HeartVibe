import secrets
import string
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from django.core.cache import cache
from .models import OTP


def generate_otp():
    return ''.join(secrets.choice(string.digits) for _ in range(6))


def send_otp_email(user_email):
    # Проверяем, когда последний раз отправляли код
    last_sent = cache.get(f"otp_last_sent_{user_email}")
    if last_sent and (now() - last_sent).seconds < 60:  # Ждём 60 секунд
        raise Exception("Слишком частые запросы. Попробуйте позже.")

    otp_code = generate_otp()

    otp, created = OTP.objects.update_or_create(
        email=user_email,
        defaults={'code': otp_code, 'created_at': now()}
    )

    subject = 'Ваш OTP код для подтверждения email'
    message = f"Ваш OTP код: {otp_code}. Код действует 5 минут."

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )

        # Сохраняем время последней отправки в кэше
        cache.set(f"otp_last_sent_{user_email}", now(), timeout=60)  # 60 секунд блокировки

    except Exception as e:
        raise Exception(f"Ошибка при отправке email: {str(e)}")
