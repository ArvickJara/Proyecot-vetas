from django.db import models

# Create your models here.

TIPO_OPCIONES = {
    ("N", "Natural"),
    ("J", "Juridica")
}

class Cliente(models.Model):
    documento =models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    ap = models.CharField(max_length=25)
    am = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    tipo = models.CharField(max_length=1, choices=TIPO_OPCIONES)

    def __str__(self):
        return self.documento +" - "+ self.ap + " "+ self.am + ", "+self.nombre
    
    def nombreCompleto(self):
        return self.ap + " "+ self.am + ", "+self.nombre


class Producto(models.Model):
    codigo =models.CharField(max_length=10)
    nombreProdc = models.CharField(max_length=120)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombreProdc
    
class Marca(models.Model):
    
    marca = models.CharField(max_length=25)

    def __str__(self):
        return self.marca   

class Modelo(models.Model):

    modelo = models.CharField(max_length=45)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

#class Categoria(models.Model):

#class Productos(models.Model):  lsita de precios carrito de compras -> la siguiente semana terminaremos esto.