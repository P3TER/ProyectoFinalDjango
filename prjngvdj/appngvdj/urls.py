from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='index'),
    path('pedido/', views.agregarPedido, name='hacerPedido'),
    path('clientes/', views.agregarClientes, name='clientes'),
    path('libros/', views.agregarLibro, name='libro'),
    path('autores/', views.agregarAutor, name='autor'),
    path('misPedidos/', views.visualizarPedidos, name='pedidos'),
    path('editarPedido/<int:idPedido>/', views.modificarPedido, name='modPedido'),
    path('editarLibro/<int:isbn>/', views.modificarLibro, name='modLibro'),
    path('editarAutor/<int:id_autor>/', views.modificarAutor, name='modAutor'),
    path('editarCliente/<int:idCliente>/', views.modificarCliente, name='modCliente'),
    path('eliminarPedido/<int:idPedido>/', views.eliminarPedido, name='elimPedido'),
]
