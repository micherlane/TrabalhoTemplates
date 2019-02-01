from django.conf.urls import url
from .views import Home,CadastroCliente,ListaCliente

urlpatterns = [
   url(r'^$',CadastroCliente,name='Página Principal'),
   url(r'^$',ListaCliente.as_view(),name='ListaCliente'),
]
