from operator import truediv
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from administracion.models import *
from administracion.forms import *
# Create your views here.


def inicio(request):
    return render(request, "base.html")


def empleados(request):
    return render(request, "empleados.html")


def clientes(request):
    return render(request, "clientes.html")


def productos(request):
    return render(request, "productos.html")


def ver_empleados(request):

    empleados = Empleados.objects.all()
    dicc = {"empleados": empleados}
    plantilla = loader.get_template("tabla_emp.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


"""---------EMPLEADOS------------"""


def add_empleado(request):

    if request.method == "POST":

        mi_formulario = Empleado_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            print(datos)
        empleado = Empleados(
            nombre=datos['nombre'], apellido=datos['apellido'], dni=datos['dni'])
        empleado.save()

        return render(request, "empleados.html")

    return render(request)


def buscar_emp(request):
    comprobar = request.GET
    print(comprobar)
    if 'nombre' in comprobar.keys():
        print("llegamos", comprobar)
        empleado = Empleados.objects.filter(nombre__icontains=comprobar)
        print(empleado)
        return render(request, "busqueda_emp.html", {"empleados": empleado})
    elif 'apellido' in comprobar.keys():
        empleado = Empleados.objects.filter(apellido__icontains=comprobar)
        return render(request, "busqueda_emp.html", {"empleados": empleado})
    elif 'dni' in comprobar.keys():
        empleado = Empleados.objects.filter(dni__icontains=comprobar)
        return render(request, "busqueda_emp.html", {"empleados": empleado})
    else:
        return HttpResponse("datos incorrectos")


"""---------Clientes-----------"""


def add_cliente(request):
    if request.method == "POST":

        mi_formulario = Cliente_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            cliente = Clientes(
                nombre=datos['nombre'], contacto_mail=datos['contacto_mail'], contacto_tel=datos['contacto_tel'])
            cliente.save()
            print("cliente agregado a la db")
        return render(request, "clientes.html")

    return render(request)


def buscar_client(request):
    comprobar = request.GET
    if 'nombre' in comprobar.keys():
        cliente = Clientes.objects.filter(nombre__icontains=comprobar)
        return render(request, "busqueda_client.html", {"clientes": cliente})


"""----------PRODUCTOS----------- """


def add_producto(request):
    if request.method == "POST":

        mi_formulario = Producto_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            print(datos)
            producto = Producto(nombre_producto=datos['nombre'], categoria=datos['categoria'],
                                barcode=datos['barcode'], precio=datos['precio'], stock=['stock'])
            producto.save()

        return render(request, "productos.html")

    return render(request)


def buscar_prod(request):
    comprobar = request.GET
    if 'nombre_producto' in comprobar.keys():
        producto = Empleados.objects.filter(
            nombre_producto__icontains=comprobar)
        print(producto)
        return render(request, "busqueda_prod.html", {"productos": producto})
