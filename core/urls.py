from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.projeto_list, name="projeto_list"),
    path("projetos/novo/", views.projeto_create, name="projeto_create"),
    path("projetos/<int:pk>/editar/", views.projeto_update, name="projeto_update"),
    path("projetos/<int:pk>/excluir/", views.projeto_delete, name="projeto_delete"),
    # tarefas
    path("tarefas/", views.tarefa_list, name="tarefa_list"),
    path("tarefas/novo/", views.tarefa_create, name="tarefa_create"),
    path("tarefas/<int:pk>/editar/", views.tarefa_update, name="tarefa_update"),
    path("tarefas/<int:pk>/excluir/", views.tarefa_delete, name="tarefa_delete"),
]
