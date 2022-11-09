"""
Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.

"""

#Variables
num= int(0)
cont= int(1)

###   Logica   ###

#Pedido de ingreso numero y carga variable
num= int(input("Ingrese el numero a multiplicar: "))

#Ciclo que multiplica numero ingresado
for i in range (1,11):
    print(num*i)
