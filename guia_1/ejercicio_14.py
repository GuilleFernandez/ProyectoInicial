"""
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, 
proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: 
Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar 
la dirección de mail sería: fsteffolani@umet.edu.ar. 
Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar:
 .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y 
 Dominio= colegiorosarito.edu.ar la dirección de mail sería: soledad.steffolani@umet.edu.ar
"""

#variables
nombre= ""
apellido= ""
mail=""
letra_apellido=""
letra_nombre=""

###   Logica   ###

print("Segun su nombre y apellido se le otorgara un mail con el dominio ingresado")

#Ingreso de datos por teclado
nombre= str.lower(input("Ingrese su nombre: "))
apellido= str.lower(input("Ingrese su apellido: "))
mail= str.lower(input("Ingrese el dominio. Recuerde que debe ser algo similar a umet.com.ar: "))

#carga de primer letra de nombre y apellido en variables
letra_nombre=nombre[0] 
letra_apellido=apellido[0]

#Condicionales para crear mail
if letra_apellido == letra_nombre:
    print("Su mail sera el siguiente: ")
    print(nombre+"."+apellido+"@"+mail)
else:
    print("Su mail sera el siguiente: ")
    print(letra_nombre+apellido+"@"+mail)  


"""
#impresiones de control
print(nombre)
print(apellido)
print(mail)
print(letra_nombre)
print(letra_apellido)
"""