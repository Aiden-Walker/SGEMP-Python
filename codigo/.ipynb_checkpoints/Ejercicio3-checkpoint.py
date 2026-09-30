print("Usuario, escribe la temperatura actual")
temp = int(input())
print("Usuario, la temperatura por la cual debajo de la misma se activara el termostato")
termostato = int(input())
print("Finalmente, escribe la temperatura sobre la cual se activara el aire acondicionado")
aire_acondicionado = int(input())
if temp < aire_acondicionado and temp > termostato:
    print("La temperatura es la adecuada")
elif temp > aire_acondicionado:
    print("Hace calor, se va a activar el aire acondicionado")
elif temp < termostato:
    print("Hace frio, se va a activar el termostato")