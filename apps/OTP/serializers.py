from rest_framework import serializers
from django.utils.timezone import now
from .models import OTP

class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get("email")
        code = data.get("code")

        otp = OTP.objects.filter(email=email, code=code).first()

        if not otp:
            raise serializers.ValidationError({"code": "Неверный OTP код или email."})

        # Проверяем срок действия OTP (например, 5 минут)
        if (now() - otp.created_at).seconds > 300:  # 300 секунд = 5 минут
            raise serializers.ValidationError({"code": "OTP код устарел."})

        # Удаляем OTP после успешной проверки (чтобы нельзя было использовать повторно)
        otp.delete()

        return data
