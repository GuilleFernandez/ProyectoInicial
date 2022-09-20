"""
Conversión de medidas. Desarrolle un programa para 
convertir una medida dada  en pies a sus equivalentes en: 
yardas, pulgadas, centimetros, metros
Sabiendo que: 
1 pie = 12 pulgadas 
1 yarda = 3 pies 
1 pulgada = 2.54 centímetros 
1 metro = 1000 centimetros
"""


#Variable
pie = float(0.0)

#constantes
yarda = float (0.333)
cm = float (30.48)
mt = float (0.348)

###   LOGICA   ###

#Mensaje y pedido de ingreso de datos a usuario
print ("Se convertiran desde la unidad de medida Pies hacia yardas, pulgadas y centimetros ")
pie = float (input("Ingrese la cantidad de pies a convertir: "))

#Conversiones de unidades de medidas y muestra por pantalla a usuario
print (f"Los {pie} pie ingresados equivalen a {pie * yarda} yardas" )
print (f"Los {pie} pie ingresados equivalen a {pie * cm} entimetros" )
print (f"Los {pie} pie ingresados equivalen a {pie * mt} metros" )

