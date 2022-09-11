"""
Escriba un programa que transforme todas las letras de una palabra 
en mayúsculas, minúsculas y la primera con minúsculas(capitalización).
"""


#Variables
palabra = str("")
mayuscula = str("")
minuscula =("")
primera_minuscula = ("")

###   LOGICA   ###

#Ingreso de texto por teclado
palabra = str(input("Ingrese la palabra: "))
#Conversion de texto a mayuscuka
mayuscula = palabra.upper()
#Conversion de texto a minuscula
minuscula = palabra.lower()
#Conversion de la primer letra en mayuscula
primera_minuscula = palabra.capitalize()

#Salida por pantalla
print(f"La palabra ingresda es: {palabra}")
print(f"La palabra en mayuscula es: {mayuscula} ")
print(f"La palabra en minuscula es: {minuscula}") 
print (f"Con la primera letra en mayuscula: {primera_minuscula}" )
