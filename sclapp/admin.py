from django.contrib import admin
from .models import Orgao, Licitante, Licitacao

# Register your models here.
admin.site.register(Orgao)
admin.site.register(Licitante)
admin.site.register(Licitacao)
