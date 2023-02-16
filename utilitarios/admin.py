from django.contrib import admin
from .models import Pessoa, Bloco, Setor, ListaFone, Area

# Register your models here.

@admin.register(Pessoa)
class PessoAdmin(admin.ModelAdmin):
    list_display = ()
    fields = []


@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    list_display = ()
    fields = []


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ()
    fields = []


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ()
    fields = []


@admin.register(ListaFone)
class ListaFoneAdmin(admin.ModelAdmin):
    list_display = ('pessoaLista', 'fone', 'area', 'bloco', 'setor')
    fields = []

