numero=[1,2,3,4,5,6,7]

print(numero)
arreglo=[1,'hola',4, 'Ronal',1,2,3,4,5,6,7]
print(arreglo)

# Conoce el numero de elementos del estado
print(len(arreglo))

# imprimir el ultimo elemento 
print(arreglo[len(arreglo)-1])

# otra forma de imprimir el ultimo elemento
print(arreglo[-1])

# para imprimir el penuntimo numero 
print(arreglo[-2]) 

# agregamos un elemento al final 
arreglo.append("figueroa")
print(arreglo)

# count imprime el numero de veces que se encuentra
print(arreglo.count("profe"))

# imprime todos los elementos menos el primero y el último
arreglolice=arreglo[1:-1]
print(arreglolice)

# insertar en el indice 5, un elemento
arreglo.insert(5,"ingenieria")
print(arreglo)

letras=['B','A','E','Z','b' 'R']
print(letras)

# ordena las letras del abecedario
letras.sort()
print(letras)

# adiciona los elementos de otras arraylis 
letras.extend(arreglo)
print(letras)

#localizar y buscar la letra en la posicion 
letras.index('R')
print(letras)

# invierte los elementos de una lista 
letras.reverse()

# elimina un elemento de lista 
letras.remove("ronal") 
