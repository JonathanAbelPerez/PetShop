from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.inicio, name='administracion'),
    path("empleados", views.empleados, name='empleados'),
    path("clientes", views.clientes, name="clientes"),
    path("productos", views.productos, name="productos"),
    path("add_empleado", views.add_empleado),
    path("ver_empleados", views.ver_empleados, name="ver_empleados"),
    path("buscar_emp", views.buscar_emp),
    path("add_cliente", views.add_cliente, name="add_cliente"),
    path("buscar_client", views.buscar_client),
    path("add_producto", views.add_producto, name="add_producto"),
    path("buscar_prod", views.buscar_prod)

]