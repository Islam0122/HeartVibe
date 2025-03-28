from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OTPSerializer
from .utils import send_otp_email  # Функция отправки OTP
from django.core.cache import cache
from django.utils.timezone import now


class SendOTPView(APIView):
    """ Отправка OTP на email """

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if not email:
            return Response({"error": "Email не был предоставлен."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем частоту отправки (раз в 1 минуту)
        last_sent = cache.get(f"otp_last_sent_{email}")
        if last_sent and (now() - last_sent).seconds < 60:
            return Response({"error": "Слишком частые запросы. Попробуйте позже."},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)

        try:
            send_otp_email(email)  # Функция генерации и отправки OTP
            return Response({"message": "OTP был отправлен на ваш email."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    """ Подтверждение OTP """

    def post(self, request, *args, **kwargs):
        serializer = OTPSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message": "OTP подтвержден."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
