from django.urls import include, path  # Importamos las funciones include y path de Django
from rest_framework import routers  # Importamos el enrutador proporcionado por DRF

from apps.users import views  # Importamos las vistas de nuestro proyecto

# Creamos un enrutador predeterminado de DRF
router = routers.DefaultRouter()

# Registramos nuestras vistas en el enrutador
router.register(r'users', views.UserViewSet)  # Registramos el UserViewSet bajo la ruta 'users'
router.register(r'groups', views.GroupViewSet)  # Registramos el GroupViewSet bajo la ruta 'groups'

# Configuramos las URLs para nuestra API utilizando el enrutamiento automático
# Incluimos las URLs generadas por el enrutador
# Además, incluimos las URLs de inicio de sesión para la API navegable
urlpatterns = [
    path('', include(router.urls)),  # Incluimos las URLs generadas por el enrutador
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))  # Incluimos las URLs de autenticación proporcionadas por DRF
]
