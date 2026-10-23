#El Operador lógico AND (&&) devuelve verdadero (true) únicamente cuando todos los operandos o condiciones evaluadas son verdaderos. Si al menos uno de los valores es falso (false), el resultado general será falso
resultado = True & True       #Devuelve True porque ambas condiciones son verdaderas
resultado2 = True & False     #Devuelve False porque una de las condiciones es falsa
resultado3 = False & True     #Devuelve False porque una de las condiciones es falsa
resultado4 = False & False    #Devuelve False porque ambas condiciones son falsas

#El Operador lógico OR (||) devuelve verdadero (true) cuando al menos una de las condiciones evaluadas es verdadera. Si todas las condiciones son falsas, el resultado general será falso
resultado5 = True | True       #Devuelve True porque al menos una de las condiciones es verdadera
resultado6 = True | False     #Devuelve True porque al menos una de las condiciones es verdadera
resultado7 = False | True     #Devuelve True porque al menos una de las condiciones es verdadera
resultado8 = False | False    #Devuelve False porque ambas condiciones son falsas

#Not: El operador NOT (también llamado operador de negación) es un elemento lógico que invierte el valor de verdad de una expresión
resultado9 = not True        #Devuelve False porque la condición no es verdadera
resultado10 = not False      #Devuelve True porque la condición no es falsa