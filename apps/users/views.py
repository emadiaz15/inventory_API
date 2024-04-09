from django.contrib.auth.models import Group, User  # Importamos los modelos User y Group de Django
from rest_framework import permissions, viewsets  # Importamos las clases de permisos y viewsets de DRF

from apps.users.serializers import GroupSerializer, UserSerializer  # Importamos los serializadores


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')  # Consulta para obtener todos los usuarios, ordenados por fecha de unión
    serializer_class = UserSerializer  # Especificamos el serializador a utilizar para los usuarios
    permission_classes = [permissions.IsAuthenticated]  # Especificamos los permisos requeridos para acceder a esta vista


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')  # Consulta para obtener todos los grupos, ordenados por nombre
    serializer_class = GroupSerializer  # Especificamos el serializador a utilizar para los grupos
    permission_classes = [permissions.IsAuthenticated]  # Especificamos los permisos requeridos para acceder a esta vista
