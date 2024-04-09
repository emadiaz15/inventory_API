from django.contrib.auth.models import Group, User
from rest_framework import serializers

# Importaciones necesarias: User y Group son modelos de autenticación de Django,
# y serializers es la herramienta que usaremos para serializar/deserializar datos en JSON.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Definición del serializador para el modelo User
    class Meta:
        # Metadatos del serializador
        model = User  # Especificamos que el modelo a serializar es User
        fields = ['url', 'username', 'email', 'groups']
        # Campos a incluir en la representación serializada:
        # 'url': un enlace a la representación detallada del usuario
        # 'username': nombre de usuario del usuario
        # 'email': dirección de correo electrónico del usuario
        # 'groups': grupos a los que pertenece el usuario

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # Definición del serializador para el modelo Group
    class Meta:
        # Metadatos del serializador
        model = Group  # Especificamos que el modelo a serializar es Group
        fields = ['url', 'name']
        # Campos a incluir en la representación serializada:
        # 'url': un enlace a la representación detallada del grupo
        # 'name': nombre del grupo
