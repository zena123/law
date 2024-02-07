from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, exceptions, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, DocumentAttachment, LegalRequest
from .serializers import (
    ClientSerializer,
    DocumentAttachmentSerializer,
    LegalRequestSerializer,
    ClientRegistrationSerializer,
)


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['confirm_password']:
            raise exceptions.APIException("passwords don't match")

        serializer = ClientRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


csrf_exempt


class CustomLoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful', 'userRole': 'admin' if user.is_staff else 'user'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'})


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DocumentAttachmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DocumentAttachment.objects.all()
    serializer_class = DocumentAttachmentSerializer


class LegalRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LegalRequest.objects.all()
    serializer_class = LegalRequestSerializer
