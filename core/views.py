from rest_framework import viewsets, exceptions
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

        data['is_ambassador'] = 0
        serializer = ClientRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DocumentAttachmentViewSet(viewsets.ModelViewSet):
    queryset = DocumentAttachment.objects.all()
    serializer_class = DocumentAttachmentSerializer


class LegalRequestViewSet(viewsets.ModelViewSet):
    queryset = LegalRequest.objects.all()
    serializer_class = LegalRequestSerializer
