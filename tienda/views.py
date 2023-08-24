from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, View
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from django.urls import reverse_lazy
from django.views import View

class ListaCategoriasView(View):
    def get(self, request):
        categorias = Categoria.objects.all()  
        return render(request, 'tienda/lista_categorias.html', {'categorias': categorias})
    
class ListaProductosView(View):
    def get(self, request):
        productos = Producto.objects.all()  
        return render(request, 'tienda/lista_productos.html', {'productos': productos})
    
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
    model = Categoria  
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
