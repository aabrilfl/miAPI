'''
    serializers.py - Archivo donde vamos a serializar
    los distintos modelos de la aplicación
'''

from rest_framework import serializers
# Importar todos los modelos de la aplicación
from .models import Article, Contact, Publication


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'alias')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'subject', 'publications')


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'title')
