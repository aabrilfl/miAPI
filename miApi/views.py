# Django Rest Framework nos traer la ViewSets
from decimal import Context
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Serializer de nuestros modelo Contact
from .models import Publication, Article, Contact
from .serializers import ArticleSerializer, ContactSerializer, PublicationSerializer


# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('subject')
    serializer_class = ArticleSerializer


class BlogViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super(BlogViewSet, self).__init__(**kwargs)

    def list(self, request):
        publications = Publication.objects.all().order_by('title')
        serialized_data = PublicationSerializer(publications, many=True)

        return Response(serialized_data.data,
                        status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='article')
    def list_articles(self, request):
        articles = Article.objects.all().order_by('subject')
        serialized_data = ArticleSerializer(
            data=articles, context={'request': request}, many=True)
        serialized_data.is_valid()

        return Response(serialized_data.data,
                        status=status.HTTP_200_OK)
