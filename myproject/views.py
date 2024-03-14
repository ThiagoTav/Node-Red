from django.shortcuts import render
# No arquivo views.py dentro da sua pasta core
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dados
from .serializers import DadosSerializer

@api_view(['POST'])
def receber_dados(request):
    serializer = DadosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)