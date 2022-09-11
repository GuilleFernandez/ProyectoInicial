"""
Últimos dígitos ¿Cómo usaría el operador resto (%) 
para obtener el valor del último dígito de un número entero? 
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un 
programa que cargue un número entero por teclado, 
y muestre el último dígito del mismo (por un lado) 
y los dos últimos dígitos (por otro lado).
"""


#Variables

numero = int(0)
ult_digit = int (0)
dos_ult_digit = int(0)

###   LOGICA   ###

#Ingreso de numero por teclado
numero = int(input("Ingrese un numero con tres o mas digitos: "))

#calculo del ultimo digito con operador resto
ult_digit = numero % 10

#Calculo de dos ultimos digitos con operador resto
dos_ult_digit = numero % 100

#Muentra por pantalla numero ingresado, ultimo digito y dos ultimos digitos
print(f"El numero ingresado es {numero}")
print(f"el ultimo digito del numero ingresado es {ult_digit}")
print(f"Los dos ultimos digitos del numero ingresado son {dos_ult_digit}")