#Tipos de datos compuestos: son aquellos que pueden contener varios elementos de diferentes tipos de datos. Los tipos de datos compuestos más comunes en Python son las listas, tuplas, conjuntos y diccionarios.
#-----------------------------------------------------------------------------------------------------------
#Listas: son un tipo de dato compuesto, es decir, que pueden contener varios elementos de diferentes tipos de datos. Se definen usando corchetes [] y los elementos se separan por comas.
#se pueden modificar, agregar o eliminar elementos de una lista. A continuación se muestra un ejemplo de una lista:
list = ["Luis Carrillo", "Desarrollador", True, 1.73]
print(list) #Imprimir la lista completa
print(list[1]) #Acceder a un elemento de la lista, recordemos que el primer elemento esta en el índice 0, al llamar al elemento 1 imrimira desarrollador
list[2] = False #Modificar un elemento de la lista, en este caso el elemento 2 que es True, se cambia a False
print(list) #Imprimir la lista completa
print(list[2])
#-----------------------------------------------------------------------------------------------------------
#Tuplas: Son iguales que las listas, pero en vez de usar corchetes, se usan paréntesis. La diferencia es que las tuplas son inmutables, es decir, no se pueden modificar.
tuple = ("Luis Carrillo", "Desarrollador", True, 1.73)
#tuple[2] = False #Esto generará un error, ya que las tuplas no se pueden modificar
#-----------------------------------------------------------------------------------------------------------
#Conjuntos (sets): Son un tipo de dato compuesto que no permite elementos duplicados y no tienen un orden específico. Se definen usando llaves {}. A continuación se muestra un ejemplo de un conjunto:
set = {"Luis Carrillo", "Desarrollador", True, 1.73}
#Los conjuntos son inmutables, tampoco se puede acceder a los elementos por su indice
#-----------------------------------------------------------------------------------------------------------
#Diccionarios: Son un tipo de dato compuesto que permite almacenar pares de clave-valor. Se definen usando llaves {} y los elementos se separan por comas. A continuación se muestra un ejemplo de un diccionario:
#dato valor = {"nombre": "Luis Carrillo", "profesion": "Desarrollador", "activo": True, "altura": 1.73}
dictionary = {"nombre": "Luis Carrillo", "profesion": "Desarrollador", "activo": True, "altura": 1.73}
print(dictionary) #Imprimir el diccionario completo
print(dictionary["profesion"]) #Acceder a un elemento del diccionario usando su clave