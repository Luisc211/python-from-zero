# “else-if” se escribe elif (una contracción de else if). Sirve para encadenar varias condiciones, de modo que Python revise una por una hasta encontrar la primera que sea verdadera.
nota = 75
if nota >= 90:
    print("Excelente")
elif nota >= 72:
    print("Aprobado")
elif nota >= 50:
    print("Recuperación")
else:
    print("Reprobado")

# --------------------------------------------------------------------------------------------------

# Un if anidado es un if que está dentro de otro if (o de un elif o else). Sirve cuando una segunda condición solo tiene sentido revisarla después de que se cumpla la primera.
edad = 20
tiene_entrada = True
if edad >= 18:
    if tiene_entrada:
        print("Puedes entrar al evento")
    else:
        print("Puedes entrar al evento, pero necesitas una entrada")
else:
    print("No puedes entrar al evento, eres menor de edad")
