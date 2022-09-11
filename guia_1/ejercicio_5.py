"""
Área de un triángulo. Desarrolle un programa para calcular el
 área de un triángulo, cargando por teclado el valor 
 de la base, pero sabiendo que su altura es igual al 
 cuadrado de la base.
"""

#variables

base = int(0)
altura = int(0)
area = float(0.0)

###   LOGICA   ###

#Ingreso de base
base = int(input("Ingrese la base del triangulo: "))

#Calculo de altura
altura = base**2

#Calculo de area y carga en variable
area = float (base*altura)/2

#Salida por pantalla del calculo del area de un triangulo, la altura y la base ingresada
print(f"La base del triangulo es {base}")
print(f"La altura es {altura}")
print (f"El calculo del area es: {area} metros cuadrados")