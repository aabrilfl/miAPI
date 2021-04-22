'''
urls.py de miAPI donde vamos a especificar las rutas de
la API Restful
'''

from django.urls import path, include
from rest_framework import routers

# Importamos todas las Views declaradas en el archivo views.py
# de la aplicación miApi
from . import views

'''
Definimos las rutas
'''
router = routers.DefaultRouter()
# Registramos la ruta base de la api
router.register(r'contactos', views.ContactViewSet, basename='contactos')
router.register(r'blog', views.BlogViewSet, basename='blog')
router.register(r'blog/articles', views.ArticleViewSet, basename='articles')

# Especificar los urlPatterns para llegar a consumir cada endpoint
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include(
        'rest_framework.urls', namespace='rest_framework'))
]
