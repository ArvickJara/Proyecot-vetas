from django.shortcuts import render,redirect
from . import models,forms



#Cliente
#Read
def cliente(request):
    clientes = models.Cliente.objects.all()
    contexto = {'clientes': clientes, "titulo": 'Sistemas de ventas - Cliente' }
    return render(request, 'ventas_app/clientes.html', contexto)

def crearcliente(request):
    if request.method == "POST":
        formulario = forms.ClienteForm.ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/clientes/')
    formulario = forms.ClienteForm
    contexto = {"form": formulario, "titulo" : "Crear nuevo cliente"}
    return render(request, "ventas_app/crearcliente.html", contexto)


def actualizarclientes (request, id):
    cliente = models.Cliente.objects.get(id=id)
    if request.method == "POST":
        formulario = forms.ClienteForm.ClienteForm(request.POST,instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('/clientes/')
    formulario = forms.ClienteForm(instance=cliente)
    contexto = {"form": formulario}
    return render(request, "ventas_app/crearcliente.html", contexto)

def eliminarclientes (_request, id):
    cliente = models.Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes/')

#Marca
#Read
def marca(request):
    marcas = models.Marca.objects.all()
    contexto = {'marcas': marcas, "titulo": 'Sistemas de ventas - Marcas' }
    return render(request, 'ventas_app/marcas.html', contexto)

#create
def crearmarca(request):
    if request.method == "POST":
        formulario = forms.MarcaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/marcas/')
    formulario = forms.MarcaForm
    contexto = {"form": formulario, "titulo" : "Crear nueva marca"}
    return render(request, "ventas_app/crearmarcas.html", contexto)

def actualizarmarca (request, id):
    marca = models.Marca.objects.get(id=id)
    if request.method == "POST":
        formulario = forms.MarcaForm(request.POST,instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect('/marcas/')
    formulario = forms.MarcaForm(instance=marca)
    contexto = {"form": formulario, "titulo" : "Actualizar Marca"}
    return render(request, "ventas_app/crearmarcas.html", contexto)

def eliminarmarca (request, id):
    marca = models.Marca.objects.get(id=id)
    marca.delete()
    return redirect('/marca/')
# Create your views here.
