from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from rest_framework import status, mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.decorators import action

from django.contrib.auth import get_user_model
from django.views import View
from django.utils.decorators import method_decorator

from accounts.serializers import SignupSerializer, TokenObtainPairResponseSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class DecoratedTokenObtainPairView(TokenObtainPairView):
    # @extend_schema(
    #     request=TokenObtainPairResponseSerializer,
    #     responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer},
    # )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SignUpUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer
    
    # @extend_schema(
    #     request=SignupSerializer,
    #     responses={status.HTTP_200_OK: SignupSerializer},
    # )
    # @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)