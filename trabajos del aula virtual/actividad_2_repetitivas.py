#actividad 1: hacer un cuadrado de asteriscos
tam = int(input("ingrese el tamaño del cuadrado: "))
for i in range(tam):
    for j in range(tam):
        print("*", end = "")
    print()

#acividad 2: triangulo ascendente:
numero = int(input("ingrese un numero: "))
for i in range(1,numero + 1):
    for j in range(1, i + 1):
        print(j, end = "")
    print()

#actividad 3: tablas demultiplicar anidadas:

for i in range(1,11):
    for j in range(1,11):
        print(i ,"x", j,"=", i*j, end ="")
        print()
    
#actividad 4:cuadrado con bordes 1 e interior 0:

n = int(input("ingrese el tamaño del cuadrado:"))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n -1:
            print(1, end = "")
        else:
            print(0, end = "")
    print()

#actividad 5: combinacion de coordenadas:

for x in range(3):
    for y in range(3):
        for z in range(3):
            print(f"({x}, {y}, {z})")

#actividad 6: combinaciones con suma 10:

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i + j + k == 10:
                print(f"{i} + {j} + {k} = 10")

#actividad 7: contador regresivo 333-000:

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        for k in range(3, -1, -1):
            print(i,j,k)

#actividad 8: reloj digital

        
#actividad 9:lanzamiento de dado:

import random

jugar = input("quieres jugar a lanzar un dado y ver en cuanto sacas 6? (s/n) ").lower
while jugar == "s":
    contador_intentos = 0
    tirar_dado = random.randint(1,6)
    if tirar_dado != 6:
        contador_intentos += 1
        print( "No salio 6 :(")
    else:
        print(f"Ha salido 6!, has tardado {contador_intentos}")
jugar = input("deseas volver a jugar? (s/n)").lower
