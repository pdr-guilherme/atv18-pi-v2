from django.contrib import admin

from core.models import Projeto, Tarefa


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "data_inicio")
    search_fields = ("nome", "descricao")


class TarefaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "prioridade", "concluido")
    search_fields = ("titulo",)
    list_filter = ("prioridade", "concluido")


admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Tarefa, TarefaAdmin)
