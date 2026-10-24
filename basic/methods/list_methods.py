
#!-----La función list crea una nueva lista, no es un metodo-----
lista = list(["Hola","Luis", 30 ])
print(lista)

#!-----Conteo de elementos de la lista-----
len(lista) #len() devuelve la cantidad de elementos en la lista.
print("Cantidad de elementos en la lista: " , len(lista))

#!-----Agregar y eliminar elementos de la lista, y limpiar toda la lista-----
lista.append("Python") #append() agrega un elemento al final de la lista.
print("Lista después de agregar un elemento con append: " , lista)

lista.insert(2, "Mundo") #insert() agrega un elemento en la posición indicada.
print("Lista después de agregar un elemento en la posición 2 con insert: " , lista)

lista.extend([True, "Programación"]) #extend() agrega varios elementos al final de la lista, deben ir dentro de corchetes.
print("Lista después de agregar varios elementos con extend: " , lista)

lista.pop(0) #pop() elimina el elemento en la posición indicada y lo devuelve. Si no se indica posición, elimina el último elemento, si queremos eliminar especificamente el ultimo elemento, le damas como parametro -1, -2 el anteultimo y así sucesivamente.
print("Lista después de eliminar el primer elemento con pop: " , lista)

lista.remove("Programación") #remove() elimina el primer elemento que coincida con el valor indicado, si no encuentra coincidencia, lanza un error.
print("Lista después de eliminar el elemento 'Programación' con remove: " , lista)

#todo lista.clear() #clear() elimina todos los elementos de la lista.
#todo print("Lista después de eliminar todos los elementos con clear: " , lista)

#!-----Ordenando la lista de menor a mayor, e invirtiendo el orden-----
#todo lista.sort() #sort ordena la lista de menor a mayor, pero solo funciona si no hay strings en dicha
#lista, acepta True y False, los False, primero, los True después, y los números luego, si le damos
#como párametro reverse=True ordena la lista de mayor a menor, es decir invierte el orden

lista.reverse() #reverse invierte el orden de la lista, pero a diferencia de sort lo hace es de acuerdo al orden de los elementos en la lista más no de menor a mayor o mayor a menor, si no de primero a ultimo, en este caso si acepta strings dentro de la lista, digamos que solo voltea el orden de las cajas sin importarle que hay dentro de ellas.
print("Orden de la lista invertida con reverse: ", lista)