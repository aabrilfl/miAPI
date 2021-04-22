from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Article(models.Model):
    subject = models.CharField(max_length=20)
    publications = models.ManyToManyField(to=Publication)
