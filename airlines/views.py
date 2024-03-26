from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Airline, Aircraft
from .serializers import AirlineSerializer, AircraftSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['POST'])
def obtain_auth_token(request):
    # Kullanıcı adı ve parola isteğinden ilgili verileri alın
    username = request.data.get('username')
    password = request.data.get('password')

    # Kullanıcı adı ve parola doğrulanırsa, bir token oluşturun
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_airline(request):
    serializer = AirlineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
def update_airline(request, airline_id):
    try:
        airline = Airline.objects.get(id=airline_id)
    except Airline.DoesNotExist:
        return Response({"error": "Airline not found"}, status=404)

    serializer = AirlineSerializer(airline, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def retrieve_airline(request, airline_id):
    if request.method == 'GET':
        try:
            airline = Airline.objects.get(id=airline_id)
            serializer = AirlineSerializer(airline)
            return Response(serializer.data, status=200)
        except Airline.DoesNotExist:
            return Response({"error": "Airline not found"}, status=404)


@api_view(['GET'])
def list_airlines(request):
    airlines = Airline.objects.all()
    serializer = AirlineSerializer(airlines, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_aircraft(request):
    serializer = AircraftSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
def update_aircraft(request, aircraft_id):
    try:
        aircraft = Aircraft.objects.get(id=aircraft_id)
    except Aircraft.DoesNotExist:
        return Response({"error": "Aircraft not found"}, status=404)

    serializer = AircraftSerializer(aircraft, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def retrieve_aircraft(request, aircraft_id):
    try:
        aircraft = Aircraft.objects.get(id=aircraft_id)
    except Aircraft.DoesNotExist:
        return Response({"error": "Aircraft not found"}, status=404)

    serializer = AircraftSerializer(aircraft)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def delete_aircraft(request, aircraft_id):
    try:
        aircraft = Aircraft.objects.get(id=aircraft_id)
    except Aircraft.DoesNotExist:
        return Response({"error": "Aircraft not found"}, status=404)

    aircraft.delete()
    return Response(status=204)


@api_view(['POST'])
def delete_airline(request, airline_id):
    try:
        airline = Airline.objects.get(id=airline_id)
    except Airline.DoesNotExist:
        return Response({"error": "Airline not found"}, status=404)

    airline.delete()
    return Response(status=204)
