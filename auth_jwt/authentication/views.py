""" Views de authenticacion """
from rest_framework import (
    mixins,
    status,
    permissions
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User

from authentication.serializers import (
    CreateUserSerializer,
    UserSerializer
)


class UserView(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               GenericViewSet):
    """API del usuario, puede ver el usuario
    logueado y actualizar el mismo"""

    queryset = User.objects.filter()
    lookup_field = 'username'
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def retrieve(self, request, *args, **kwargs):
        """ Override del metodo retrive, si el usuario que solicita
        entrar al detalle no es el que está logueado da error 401 """
        if request.user.username == kwargs['username']:
            return super().retrieve(request, *args, **kwargs)
        else:
            return Response(
                {"Error": "The user is not logged"},
                status=status.HTTP_401_UNAUTHORIZED,   
            )

class CreateUserView(mixins.CreateModelMixin,
                     GenericViewSet):
    """ API para creacion de usuario """
    queryset = User.objects.filter()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]
