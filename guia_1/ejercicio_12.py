"""
Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, 
si se pide en cada mes el 10% del sueldo ganado.
"""

#Variables

sueldo= 0
mes_ahorro= 0
total_ahorro= 0
mes= 1

###   Logica   ###

#bucle que pide ingreso de sueldo por teclado de 12 meses
while mes <= 12:
    sueldo= float(input(f"Ingrese el sueldo del mes {mes}: "))
    mes_ahorro= sueldo*0.10    #Calculo ahorro (10%) del sueldo y carga en variable
    print(f"El ahorro del 10% del mes {mes} es {mes_ahorro}")   #muestra mes y el ahorro
    total_ahorro= total_ahorro+mes_ahorro   #acumulador de ahorro
    mes= mes+1  #contador para meses

print(f"El ahorro total del año es {total_ahorro} pesos")  #Muestra en pantalla ahorro total anual