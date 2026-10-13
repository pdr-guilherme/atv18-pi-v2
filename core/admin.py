from django.contrib import admin

from .models import Projeto


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "data_inicio")
    search_fields = ("nome", "descricao")


admin.site.register(Projeto, ProjetoAdmin)