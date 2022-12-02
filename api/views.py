from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers

from .models import Cliente
from .serializers import ClienteSerializer

@api_view(['GET'])
def getCliente(request):
    cliente = Cliente.objects.all()
    serializer = ClienteSerializer(cliente, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postCliente(request):
    data = request.data
    cliente = Cliente.objects.create()
    serializer = ClienteSerializer(cliente, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def putCliente(request, pk):
    data = request.data
    cliente = Cliente.objects.get(id = pk)
    serializer = ClienteSerializer(instance = cliente, data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    cliente.delete()
    return Response('Cliente eliminado')