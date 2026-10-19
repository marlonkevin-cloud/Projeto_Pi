from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('novo/', views.criar_projeto, name='criar_projeto'),
    path('editar/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),
]