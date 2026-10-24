string1 = "hola, soy Luis"
string2 = "0123456789"
string3 = "TextoSinEspacios"

#!-----Exploración de métodos disponibles para objetos, en este caso un string-----
#?-----dir no es un método de string, es una función incorporada en Python que se puede utilizar con cualquier objeto.-----
resultado = dir(string1) #La función dir() devuelve una lista de los atributos y métodos disponibles para un objeto. En este caso, devuelve todos los métodos que se pueden utilizar con el objeto string1.
print(resultado) 

#!-----Transformar minusculas y mayusculas-----
convertir_a_mayusculas = string1.upper() #Upper convierte todo el texto a mayusculas
convertir_a_minuscualas = string1.lower() #Lower convierte todo el texto a minusculas
resuldado_capitalize = string1.capitalize() #Capitalize convierte la primera letra del string en mayuscula y el resto en minusculas
print("Todo el texto a mayusculas con upper: " , convertir_a_mayusculas)
print("Todo el texto a minusculas con lower: " , convertir_a_minuscualas)
print("Primera letra del string en mayuscula con capitalize: " , resuldado_capitalize)

#!-----Busqueda y posicioón de subcadenas dentro del string-----
buscar_subcadena = string1.find("Luis") #Busca la subcadena "Luis" dentro de string1 y devuelve el índice de la primera aparición. Si no se encuentra, devuelve -1.
buscar_subcadena_con_index = string1.index("Luis") #Busca la subcadena "Luis" dentro de string1 y devuelve el índice de la primera aparición. Si no se encuentra, lanza una excepción ValueError.
print("Subcadena encontrada con find: " , buscar_subcadena)
print("Subcadena encontrada con index: " , buscar_subcadena_con_index)

#!-----Comprobación y validación de caracteres en el string-----
resultado_isnumeric = string1.isnumeric() #isnumeric() verifica si todos los caracteres en el string son numéricos. Devuelve True si todos los caracteres son dígitos, de lo contrario devuelve False.
print("Resultado de isnumeric para string1: " , resultado_isnumeric)
resultado_isnumeric2 = string2.isnumeric()
print("Resultado de isnumeric para string2: " , resultado_isnumeric2)

resultado_isalpha = string3.isalpha() #isalpha() verifica si todos los caracteres en el string son alfabéticos. Devuelve True si todos los caracteres son letras, de lo contrario devuelve False, si hay espacios o caracteres especielaes también devuelve False.
print("Resultado de isalpha para string3: " , resultado_isalpha)

#!-----Contar coincidencias y longitud del string-----
contar_coincidencias = string1.count("o") #count() cuenta el número de veces que aparece una subcadena en el string.
contar_caracteres = len(string1)  #len() devuelve la longitud del string.
print("Número de caracteres: " , contar_caracteres)
print("Número de coincidencias: " , contar_coincidencias)

#!-----Verificar si el string comienza o termina con una subcadena específica devuelve True o False-----
empieza_con = string1.startswith("hola") #startswith() verifica si el string comienza con la subcadena especificada. Devuelve True si es así, de lo contrario devuelve False.
termina_con = string1.endswith("Luis") #endswith() verifica si el string termina con la subcadena especificada. Devuelve True si es así, de lo contrario devuelve False.
print("Empieza con 'hola': " , empieza_con)
print("Termina con 'Luis': " , termina_con)

#!-----Reemplazo y división de cadenas-----
cadena_nueva = string1.replace("Luis", "Juan") #replace() reemplaza todas las apariciones de una subcadena con otra.
cadena_separada = string1.split(",") #split() divide el string en una lista de subcadenas utilizando el separador especificado.
print("Cadena nueva con replace: " , cadena_nueva)
print("Cadena separada con split: " , cadena_separada)
