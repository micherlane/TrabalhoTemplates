from django.shortcuts import render,redirect
from .forms import test
from django.views.generic import ListView
from  .models import Cliente

def Home(request):
    return render(request,'base.html')

def CadastroCliente(request):
    form = test(request.POST)
    if form.is_valid():
        form.save()
        redirect('ListaCliente')
    else:
        form = test()
        return render(request,'index.html',{'form':form})

class ListaCliente(ListView):
    model = Cliente
    template_name = 'ListaCliente.html'
    context_object_name = 'Clientes'
    queryset = Cliente.objects.all()
