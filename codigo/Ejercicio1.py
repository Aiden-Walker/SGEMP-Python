import random
numero_a_adivinar = random.randint(10, 20))
print("Usuario, intenta adivinar el numero aleatorio del 0 al 10")
numero_usuario = input()
if numero_usuario == numero_a_adivinar:
    print ("Felicidades, has adivinado el numero")
elif numero_usuario < numero_a_adivinar:
    print ("El numero que has puesto es mas grande que el numero que debes adivinar")
elif numero_usuario > numero_a_Adivinar:
    print("El numero que has puesto es mas pequeño que el nuemro que debes adivinar")