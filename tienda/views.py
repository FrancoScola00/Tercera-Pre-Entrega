from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from django.urls import reverse_lazy

# Resto de tus vistas aquí


class BuscarView(ListView):
    model = Producto
    template_name = 'tienda/buscar.html'
    context_object_name = 'productos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Producto.objects.filter(nombre__icontains=query)
        return Producto.objects.none()

class IndexView(TemplateView):
    model = Categoria  # Asegúrate de usar el modelo correcto
    template_name = 'tienda/index.html'
    context_object_name = 'categorias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  
        return context

class AgregarProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda/agregar_producto.html'
    success_url = '/'

class AgregarCategoriaView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'tienda/agregar_categoria.html'
    success_url = '/'

class EliminarCategoriaView(DeleteView):
    model = Categoria
    template_name = 'tienda/eliminar_categoria.html'
    success_url = reverse_lazy('tienda:index')
