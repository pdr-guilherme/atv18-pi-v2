from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.projeto_list, name='projeto_list'),
    path('projetos/novo/', views.projeto_create, name='projeto_create'),
    path('projetos/<int:pk>/editar/', views.projeto_update, name='projeto_update'),
    path('projetos/<int:pk>/excluir/', views.projeto_delete, name='projeto_delete'),
]