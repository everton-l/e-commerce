from django.contrib import admin
from .models import Marca, Categoria, Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor', 'imagem')

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)