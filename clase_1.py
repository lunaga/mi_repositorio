#listas

# lista = ['1', 1, 2, 3, 'pepe', 'hola', 'casa']

#listas y strings

# cadena = 'soy una cadena cualquiera'

# print(cadena)
# print(lista)
# print(cadena[-1])
# print(lista[-1])

#funciones de listas

# append

# lista.append('otro dato')
# print(lista)

#len

# print(len(cadena))
# print(len(lista))


#pop

# print(lista)
# valor_extraido1 = lista.pop()
# print(valor_extraido1)
# print(lista)
# valor_extraido2 = lista.pop(3)
# print(valor_extraido2)

#count

# print(lista.count(1))
# lista.append(1)
# print(lista)
# print(lista.count(1))

#index

# lista.append('1')
# print(len(lista))
# print(lista.index('1', 2))

# Ejercicio de listas 

#dada dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

# - Añade a la LISTA1 el int 1234 y luego el string “Hola”
# - Añade a la LISTA2 el string “Adios” y luego el int 1234
# - Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
# - Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
# - Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

# lista1 = [1, 12, 123]
# lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# lista_1 = [1, 12, 123]
# lista_2 = ['bye', 'ciao', 'agur', 'adieu']
# lista_3 = []
# lista_4 = []
# lista_5 = []

# lista_1 = lista_1 + [1234, 'hola']
# print(lista_1)

# lista_2.append('adios')
# lista_2.append(1234)
# print(lista_2)

# lista_3 = lista_1[:-1]
# print(lista_3)

# lista_4 = lista_2[1:-1]
# print(lista_4)

# lista_5 = lista_4 + lista_3
# print(lista_5)

# tuplas

# tupla = ('otra', 1, 2, 'otra')
# tupla2 = ('menos', 54, 13, 'mas')
# tupla[2] = 'mas' #genera un error

# funciones de tuplas

# len
 
#  print(len(tupla))

# count

#  print(tupla.count('otra'))

# index

#  print(tupla.index('otra'))
#  print(tupla.index(3)) #genera un error

#  otra_tupla = tupla + tupla2
#  print(otra_tupla)


# anidacion

# mas_tupla = ((1, 2, 3), ['hola', 'pepe'])
# mas_lista = [('soy', 'una', 'tupla'), 2, 3, 4[]]
# print(mas_tupla)
# print(mas_lista)

# print(mas_tupla[1][1])

# otra_forma = 1, 2, 3, 4, 'otros valores'
# print(otra_forma)

# tupla_solo_valor = 'string'
# print(tupla_solo_valor)

# casting

# lista_desde_tupla = list(tupla_solo_valor)
# print(lista_desde_tupla)
# tupla_desde_lista = tuple(lista_desde_tuple)
# print(tupla_desde_lista)



# Ejercicio 2 (10 min)
# A partir de una variable llamada tupla debes 
# imprimir por pantalla de forma ordenada, lo siguiente:
# - El último ítem de tupla
# - El número de ítems de tupla
# - La posición donde se encuentra el ítem 87 de tupla
# - Una lista con los últimos tres ítems de tupla
# - Un ítem que haya en la posición 8 de tupla
# - El número de veces que el ítem 7 aparece en tupla
# Copia esta tupla:
tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

print(tupla[-1])

print(len(tupla))

print(tupla.index(87))

lista_de_tupla_cortada = list(tupla[-3:])
print(lista_de_tupla_cortada)

posicion_8 = tupla[7]

print(tupla[7])
# print(tupla.count())