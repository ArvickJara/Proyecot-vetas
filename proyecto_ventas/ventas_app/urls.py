from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente),
    path('crearcliente/', views.crearcliente),
    path('actualizarclientes/<int:id>',views.actualizarclientes,name='actualizarclientes'),
    path('eliminarclientes/<int:id>',views.eliminarclientes, name='eliminarclientes'),

    #Marca
    path('marcas/', views.marca),
    path('crearmarcas/', views.crearmarca),
    path('actualizarmarca/<int:id>',views.actualizarmarca,name='actualizarmarcas'),
    path('eliminarmarca/<int:id>',views.eliminarmarca, name='eliminarmarcas'),

     #Modelos
    path('modelos/', views.modelo),
    path('crearmodelos/', views.crearmodelo),
    path('actualizarmodelos/<int:id>',views.actualizarmodelo,name='actualizarmodelos'),
    path('eliminarmodelos/<int:id>',views.eliminarmodelo, name='eliminarmodelos'),

]

