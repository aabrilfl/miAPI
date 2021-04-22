from django.contrib import admin
# Importaremos el Modelo que vamos a registrar
from .models import Article, Contact, Publication

# Register your models here.

# Registramos el modelo
admin.site.register(Contact)
admin.site.register(Publication)
admin.site.register(Article)
