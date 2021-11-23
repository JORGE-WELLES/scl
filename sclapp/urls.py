from django.urls import path

from sclapp import views

urlpatterns = [
    path('cadastro', views.cad_orgao, name='cadastro'),
    path('alteracao/<int:id>/', views.alt_orgao, name='alteracao'),
    path('listar_empresa', views.list_orgao, name='listar_empresa'),
    path('', views.index, name='index'),
]