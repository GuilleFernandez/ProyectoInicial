"""
Crear un conversor de pies y pulgadas a centímetros.

""" 

#Variables y constantes
pies= 30.48
cant_pies= 0
pulgadas= 2.54
cant_pulg= 0
resultado= 0
opcion= 0


###   Logica   ###

#Impresion de opciones
print("""Ingrese la medida que desea convertir a centimetros 
1- PIES
2- PULGADAS""")
#Ingreso de opcion
opcion= int(input("Ingrese la opcion: "))

#Condicionales con calculos de pasajes de medidas
if opcion == 1:
    cant_pies= float(input("Ingrese los pies a convertir: "))
    resultado= cant_pies*pies
    print(f"La cantidad de {cant_pies} pies equivale a {resultado} centimetros")
else:
    cant_pulg= float(input("Ingrese las pulgadas a convertir: "))
    resultado= cant_pulg*pulgadas
    print(f"La cantidad de {cant_pulg} pulgadas equivale a {resultado} centimetros") 