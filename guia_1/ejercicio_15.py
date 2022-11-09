"""
Suma - División - Potencia. Se necesita desarrollar un programa que 
permita calcular la suma de tres números. Si el resultado es mayor a 
10 dividir por 2 (mostrar su resultado sin decimales), en caso 
contrario elevar el resultado al cubo
"""

#variables

from __future__ import division


num1= 0
num2= 0
num3= 0
suma= 0

print("Ingrese tres numeros para sumarlos. Si es mayor a 10 se dividen por 2, en caso contrario se eleva al cubo")
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))

suma= num1+num2+num3

if suma > 10:
    division= suma/2
    print(division)
else:
    potencia= suma**3
    print(potencia)    