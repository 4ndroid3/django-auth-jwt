""" Views de authenticacion """
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User

from authentication.serializers import UserSerializer


class UserView(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               GenericViewSet):
    """API del usuario, puede ver el usuario logueado
    crear usuarios nuevos, actualizar el usuario logueado"""
    queryset = User.objects.filter()
    lookup_field = 'username'
    serializer_class = UserSerializer



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