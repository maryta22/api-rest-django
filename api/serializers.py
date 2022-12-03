from rest_framework import serializers
from .models import Cliente, Cuenta
from django_countries.serializers import CountryFieldMixin

class ClienteSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ['cuenta']

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'
