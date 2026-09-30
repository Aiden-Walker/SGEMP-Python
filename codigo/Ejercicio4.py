print("Usuario, introduce el dia")
dia = int(input())
print("Usuario, introduce el mes")
mes = int(input())
print("Usuario, escribe el año actual")
anyo = int(input())
if mes == 1:
    mes = str("Enero")
elif mes == 2:
    mes = str("Febrero")
elif mes == 3:
    mes = str("Marzo")
elif mes == 4:
    mes = str("Abril")
elif mes == 5:
    mes = str("Mayo")
elif mes == 6:
    mes = str("Junio")
elif mes == 7:
    mes = str("Julio")
elif mes == 8:
    mes = str("Agosto")
elif mes == 9:
    mes = str("Septiembre")
    # Does anybody remember the song "september"?
elif mes == 10:
    mes = str("Octubre")
elif mes == 11:
    mes = str("Noviembre")
elif mes == 12:
    mes = str("Diciembro")
print("La fecha que has escrito")
print(dia , mes , anyo)