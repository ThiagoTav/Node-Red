# No arquivo serializers.py dentro da sua pasta core

from rest_framework import serializers
from .models import Dados

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = '__all__'
