"""
Escribir un programa que pregunte un nombre de usuario, 
y que después muestre por pantalla si su cantidad de letras 
es par o impar.
"""

#Variables
nombre = str ("")
total_caracteres = int(0)

###   LOGICA   ###

#Ingreseo de nombre por teclado
nombre = input("Ingrese su nombre: ")
#contar caracteres del nombre y guarda en variable
total_caracteres = len(nombre)

#Division de la cantidad de letras. Si el resto es 0 indica que es par, sino es impar y muestra por pantalla
if total_caracteres % 2 == 0:
    print (f"Su nombre {nombre} tiene {total_caracteres} letras y es par")
else:
    print (f"La cantidad de letras de su nombre es {total_caracteres} y es impar")