from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Airline, Aircraft


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


# Özel Token Alma Serializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # İsteğe bağlı olarak, kullanıcıdan farklı alanlar almak için serializer'ı özelleştirebilirsiniz
    pass
