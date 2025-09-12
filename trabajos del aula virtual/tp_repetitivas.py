#actividad 1

for i in range(101):
    print(i,end ="")
    print()

#actividad 2

num = int(input("Ingrese un número entero: "))
contador = 0

if num == 0:
    contador = 1
else:
    while num > 0:
        num //= 10
        contador += 1

print(f"El número tiene {contador} dígitos")

#actividad 3

num_1 = int(input("ingrese un numero: "))
num_2 = int(input("Ingrese un segundo numero: "))
suma = 0
if num_1 < num_2:
    for i in range(num_1 + 1,num_2):
        suma += i
elif num_2 < num_1:
    for i in range(num_2 + 1,num_1):
        suma +=i
else:
    print("error en los numeros")

print(f"la suma de los numeros es: {suma}")

#Actividad 4

condicion = True
suma = 0

while condicion == True:
    num = int(input("ingrese un numero entero distinto a 0 para sumar, cuando desee terminar la operacion ingrese 0: "))
    if num != 0:
        suma += num
    else:
        condicion = False

print(f"la suma de los numeros es: {suma}")

#actividad 5

import random

opcion = input("jugamos un juego? (s/n): ").lower()
print("yo voy a elegir un numero al azar entre 1 y 9 y vos vas a adivinar!!")
while opcion == "s":
    numero = random.randint(1,9)
    completado = True
    intentos = 1
    while completado == True:
        intento_usuario = int(input("ingresa un numero entre 1 y 9: "))
        if intento_usuario != numero:
             print("todavia no lo adivinas!!")
             intentos+= 1
        elif intento_usuario == numero:
            completado = False
    print(f"FELICIDADES!!, completaste el juego en {intentos} intentos")
    opcion = input("deseas volver a jugar? (s/n: )")

