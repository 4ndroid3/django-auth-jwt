
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth.models import User


class RegisterView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """View para registrar usuarios"""
    queryset = User.objects.filter().order_by('nombre')
    serializer_class = UserSerializer