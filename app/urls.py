from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^cadastrar_fornecedor', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    url(r'^lista_fornecedor', fornecedor_list, name='fornecedor_list'),
    url(r'^editar_fornecedor/(?P<pk>[0-9]+)', editar_fornecedor, name='editar_fornecedor'),
    url(r'^remover_fornecedor/(?P<pk>[0-9]+)', remover_fornecedor, name='remover_fornecedor'),
]

