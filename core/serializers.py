from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from .models import Client, DocumentAttachment, LegalRequest


class LegalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalRequest
        fields = '__all__'


class ClientRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ['email', 'name', 'phone', 'password',]

    extra_kwargs = {
        'password': {'write_only': True}
    }

    def create(self, validated_data):
        password = validated_data.get('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):
    requests = LegalRequestSerializer(many=True)

    class Meta:
        model = Client
        fields = ['email', 'name', 'phone', 'requests',]


class DocumentAttachmentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )

    class Meta:
        model = DocumentAttachment
        fields = '__all__'

    def create(self, validated_data):
        document_file = validated_data.pop('document')
        document_attachment = DocumentAttachment.objects.create(**validated_data)
        document_attachment.document.save(document_file.name, document_file, save=True)
        return document_attachment


