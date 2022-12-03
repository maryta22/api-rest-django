import decimal
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cliente, Cuenta
from .serializers import ClienteSerializer, CuentaSerializer

@api_view(['GET'])
def getCliente(request):
    cliente = Cliente.objects.all()
    serializer = ClienteSerializer(cliente, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postCliente(request):
    data = request.data
    nuevaCuenta = Cuenta.objects.create(saldo = data["saldo"])
    cliente = Cliente.objects.create(cuenta = nuevaCuenta)
    serializer = ClienteSerializer(cliente, data = data, many = False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def putCliente(request, pk):
    data = request.data
    cliente = Cliente.objects.get(id = pk)
    serializer = ClienteSerializer(cliente, data = data, many = False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    cliente.delete()
    return Response('Cliente eliminado')

@api_view(['PUT'])
def editarSaldo(request, pk, accion):
    data = request.data
    cliente = Cliente.objects.get(id = pk)
    cuenta = Cuenta.objects.get(id = cliente.cuenta.id)
    cantidad = decimal.Decimal(data["saldo"]).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)
    if accion == "depositar":
        data["saldo"] = cuenta.saldo + cantidad
    elif (accion == "retirar") & ((cantidad.compare(cuenta.saldo) == decimal.Decimal('-1')) |  (cantidad.compare(cuenta.saldo) == decimal.Decimal('0'))):
            data["saldo"] = cuenta.saldo - cantidad
    else:
        data["saldo"] = cuenta.saldo
    serializer = CuentaSerializer(cuenta, data = data, many = False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)