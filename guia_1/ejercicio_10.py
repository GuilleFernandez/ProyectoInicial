"""
Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto.
"""

#Variables
num1= int(0)
num2= int(0)
cociente= (0)
resto= (0)

###   Logica   ###

#Pedido de numeros a usuario y carga de variables
num1= int(input("Ingrese el primer numero a divivir: "))
num2= int(input("Ingrese el segundo numero a divivir: "))

#Operaciones de divisiones
cociente= float(num1/num2)
resto= int(num1%num2)

#Muentra por pantalla de resultados
print(f"El cociente de la division entre {num1} y {num2} es {cociente}")
print(f"El resto de la division entre {num1} y {num2} es {resto}")
