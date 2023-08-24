from django.contrib import admin
from django.urls import path, include
from tienda.views import IndexView  # Importa la vista IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),  # Define la ruta raíz con la vista IndexView
    path('tienda/', include('tienda.urls')),
]
