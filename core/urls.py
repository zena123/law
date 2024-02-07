from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientViewSet,
    DocumentAttachmentViewSet,
    LegalRequestViewSet,
    RegisterView,
    CustomLoginView,
    LogoutView
)

app_name = "core"

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'document-attachments', DocumentAttachmentViewSet)
router.register(r'legal-requests', LegalRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
