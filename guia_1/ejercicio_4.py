"""
Cuadrado de un binomio. Plantear un script directamente en el shell de Python, 
que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) 
es igual al cuadrado del primer término, más el doble producto del primero por 
el segundo más el cuadrado del segundo.
"""
#Libreria
import random

#Variables
num_a = int(0)
num_b = int(0)
result = float (0.0)

###   LOGICA   ###

#Numeros aleatorios para variables entre 0 y 50
num_a = random.randint(0,50)
num_b = random.randint(0,50)

#Se informa que operacion se realizara
print("Se calcula el binomio al cuadrado(suma) y su formula es: (a+b)*2=a*2+2.a.b+b*2")

#Se imprimen los numeros aleatorios
print (f"Los numeros aleatorios son {num_a} y {num_b}")

#Se calcula el binomio al cuadrado (Suma) y se guarda el resultado en variable
result = (num_a**2)+ 2*(num_a)*(num_b)+(num_b**2)

#Se imprimen nuevamente ambos numeros calculados y el resultado
print (f"El binomio al cuadrado de {num_a} y {num_b} es {result}")