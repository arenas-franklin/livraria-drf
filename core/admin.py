from django.contrib import admin

# Register your models here.

from core.models import Categoria, Editora

admin.site.register(Categoria)
admin.site.register(Editora)