from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dados
from .serializers import DadosSerializer

@api_view(['GET', 'POST'])
def receber_dados(request):
    if request.method == 'GET':
        dados = Dados.objects.all()  # Ou qualquer consulta que você desejar
        serializer = DadosSerializer(dados, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)