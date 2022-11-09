"""
Comisión de vendedores. Una empresa debe calcular el total de comisiones que debe 
abonar por ventas realizadas por sus vendedores, para ello les solicita un sistemita 
que le permita calcular dichos montos. Se tiene conocimiento que la empresa tiene 
cuatro categorías de vendedores (1 a 4).Usted debe solicitar el ingreso de la categoría
del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría
igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de 
diferentes en base a los siguientes cálculos:
Categoría1:cobra una comisión de 10%
Categoría2: cobra una comisión de 25%
Categoría3:cobra una comisión de 30%
Categoría4:cobra una comisión de 40%
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada 
categoría de vendedor es que en el la empresa junto 
con el total general.
"""
categoria=0
venta= 0
comision=0
porcentaje1=0.10
porcentaje2=0.25
porcentaje3=0.30
porcentaje4=0.40
acumulador_comision1=0
acumulador_comision2=0
acumulador_comision3=0
acumulador_comision4=0
total_general=0

while (categoria != 5):
    categoria = int(input("""Ingrese la opcion de categoria a la que pertenece
    1 - Categoria 1
    2 - Categoria 2
    3 - Categoria 3
    4 - Categoria 4
    5 - Salir

    Escriba su opcion: 
    """))
    if ( categoria == 1):
        venta = float(input("Ingrese el total de la venta: "))
        comision=venta*porcentaje1
        acumulador_comision1= comision+acumulador_comision1
        comision=0

    elif ( categoria == 2):
        venta = float(input("Ingrese el total de la venta: "))
        comision=venta*porcentaje2
        acumulador_comision2= comision+acumulador_comision2  
        comision=0  

    elif ( categoria == 3):
        venta = float(input("Ingrese el total de la venta: "))
        comision=venta*porcentaje3
        acumulador_comision3= comision+acumulador_comision3
        comision=0

    elif ( categoria == 4):
        venta = float(input("Ingrese el total de la venta: "))
        comision=venta*porcentaje4
        acumulador_comision4= comision+acumulador_comision4  
        comision=0              

    elif (categoria == 5):
        break    

total_general= acumulador_comision1+acumulador_comision2+acumulador_comision3+acumulador_comision4

print(f"El total de la comision de categoria 1 es: {acumulador_comision1}")
print(f"El total de la comision de categoria 2 es: {acumulador_comision2}")
print(f"El total de la comision de categoria 3 es: {acumulador_comision3}")
print(f"El total de la comision de categoria 4 es: {acumulador_comision4}")

print(f"El total de todas las comisiones por ventas realizadas es: {total_general}")