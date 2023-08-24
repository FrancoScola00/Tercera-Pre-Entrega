from django.contrib import admin
from django.urls import path, include
from tienda.views import IndexView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),  
    path('tienda/', include('tienda.urls')),
]
