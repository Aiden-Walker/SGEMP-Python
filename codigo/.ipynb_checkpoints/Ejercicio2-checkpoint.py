print("Usuario, escribe un numero")
numero_usuario_1 = int(input())
print("Usuario, escribe un segundo numero")
numero_usuario_2 = int(input())
print("Usuario, dime que quieres hacer")
print("1. Sumar los números.")
print("2. Restar los números.")
print("3. Multiplicar los números.")
print("4. Dividir los números. ")
numero_funcion = int(input())
if numero_funcion == 1:
    resultado = numero_usuario_1 + numero_usuario_2
    print("La suma de los dos numeros es:")
    print(resultado)
elif numero_funcion == 2:
    resultado = numero_usuario_1 - numero_usuario_2
    print(resultado)
elif numero_funcion == 3:
    resultado = numero_usuario_1 * numero_usuario_2
    print(resultado)
elif numero_funcion == 4:
    resultado = numero_usuario_1 / numero_usuario_2
    print(resultado)