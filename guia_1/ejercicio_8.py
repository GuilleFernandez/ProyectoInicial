"""
Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.
"""

#Variables
cant_num=int(0)
cont = int(3)
num1= 0
num2= 1
num3= 0

###   Logica   ###

#Mensaje y pedido de ingreso de datos
print("Se mostrara una cantidad de la sucesion de numeros de Fibonnaci")
cant_num = int(input("Ingrese la cantidad de numeros que desee ver: "))
#Muestra primer y segundo numero que se utilizan para el comienzo del calculo
print(num1)
print(num2)
#Ciclo que suma los dos terminos que le preceden y contador que se usa para cortar el ciclo
while cont <= cant_num:
    
    num3= num1+num2
    num1= num2
    num2= num3
    print(num3)
    cont = cont+1




#Sucecion de Fibonacci utilizada para comparar y controlar los datos obtenidos en pantalla
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377