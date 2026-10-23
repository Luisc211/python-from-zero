# Condicionales if else: permite que el programa tome decisiones y ejecute bloques de código según si una condición es verdadera o falsa


# if condición True
#    acción se ejecuta
##if condición False
#    acción no se ejecuta

edad = 14

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# --------------------------------------------------------------------------------------------------

contraseña_registrada = "1234567890"
contraseña_ingresda = "1234567890"

if contraseña_registrada == contraseña_ingresda:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")


print(
    "Fin del programa, este codigo se ejecuta siempre, independientemente de la condición"
)
