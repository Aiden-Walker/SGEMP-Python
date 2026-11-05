nombre_fich_ent = input("Nombre del fichero de entrada")
f = open(nombre_fich_ent,'rt')
todo = f.read()
f.close()
todo = todo.upper().replace(',','').replace('.','').replace('?','').replace(';','').replace('¿','').replace('!','').replace('¡','').replace(':','').replace('(','').replace(')','').replace('\n','')
lista_palabras = todo.split(" ")
print(lista_palabras)

diccionario = {}
for palabra in lista_palabras:
    if palabra != ' ':
        contador = diccionario.get(palabra, None)
        if contador is None:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] = contador + 1