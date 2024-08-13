import random


numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado and cant_intentos != cant_max_intentos:
    numero = int(input("Introduce un numero del 1 al 99: ")) # TO DO: convertir a numero
    

    if numero == numero_secreto:
        print("Felicidades, acertaste el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero secreto es mayor!!")
    else:
        print("El numero secreto es menor!!")
        cant_intentos += 1
    
if cant_intentos == cant_max_intentos:
    print("Perdiste, no te rindas, vuelve a intentarlo otra vez!!")