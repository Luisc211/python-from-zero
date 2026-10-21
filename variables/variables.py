# Las variables se declaran y se definen con el signo igual (=) y no necesitan ser declaradas con un tipo de dato específico, y son modificables cuantas veces se necesite.
name = "Luis"
number = 10
number += 5
number -= 3
# Concatenación de variables
saludo = f"Hola {name}, tu número es {number}"  # f string permite concatenar variables dentro de un string, conviirtiendo el valor de la variable en un string automáticamente.
# Concatenación de variables
print(saludo)

del name  # Eliminar variable
#Operadores de pertenencia in y not in
# Los operadores de pertenencia son: in y not in, que permiten verificar si un elemento pertenece o no a una secuencia (como listas, tuplas, diccionarios, etc.).
fruits = ["manzana", "banana", "naranja"]       
print("manzana" in fruits)  # True
print("uva" not in fruits)  # True

#En python se recomienda usar snake_case para nombrar variables, es decir, usar minúsculas y separar las palabras con guiones bajos. Por ejemplo: nombre_variable, edad_usuario, etc.