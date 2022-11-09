"""
Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.
"""

#variables
precio_dolar= 0
cant_dolar = 0
cant_pesos= 0
costo=0
lista=0

precio_dolar= float(input("Ingrese el precio del dolar actual: "))

print("Ingrese lo que desea cpnvertir")
print("1. Pesos a Dolares")
print("2. Dolares a Pesos")
lista= int(input("1 o 2: "))

if lista == 1:
    cant_pesos= float(input("Ingrese la cantidad de pesos a convertir: "))
    costo= cant_pesos/precio_dolar
    print(f"Los {cant_pesos} pesos equivalen a {costo} dolares")
else:
    cant_dolar= float(input("Ingrese la cantidad de dolares a convertir: "))
    costo= cant_dolar*precio_dolar
    print(f"Los {cant_dolar} dolares equivalen a {costo} pesos: ")  

