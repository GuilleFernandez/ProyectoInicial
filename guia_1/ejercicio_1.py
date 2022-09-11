"""
Desarrolle un programa que pase un peso de kilogramo a libras 
teniendo en cuenta que cada kilogramo equivale a 2.2 libras.
"""

#Variables y constantes
libra = float (2.2)
kilo = float (0.0)
result = float (0.0)

#    LOGICA  

#Ingreso de cantidad de kilos
kilo = float (input("Ingrese la cantidad de kilos: "))
#Calculo de kilos a libras
result = float(libra*kilo)
#Impresion en pantalla de ingreso por teclado y resultado
print(f"La cantidad de {kilo} kilos es {result} de libras")


