from django.urls import path
from .views import IndexView, AgregarProductoView, AgregarCategoriaView, BuscarView, EliminarCategoriaView, ListaProductosView, ListaCategoriasView

app_name = 'tienda'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('agregar_producto/', AgregarProductoView.as_view(), name='agregar_producto'),
    path('agregar_categoria/', AgregarCategoriaView.as_view(), name='agregar_categoria'),
    path('buscar/', BuscarView.as_view(), name='buscar'),
    path('eliminar_categoria/<int:pk>/', EliminarCategoriaView.as_view(), name='eliminar_categoria'),  
    path('lista_productos/', ListaProductosView.as_view(), name='lista_productos'),
    path('lista_categorias/', ListaCategoriasView.as_view(), name='lista_categorias'),
]
