from django.urls import path, include

urlpatterns = [
    path('',include('apps.users.api.urls')),
    path('api/users/', include('apps.users.api.urls')),
    path('api/products/', include('apps.products.api.urls')),
]
