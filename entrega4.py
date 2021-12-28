#1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo
# a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
#El área de un rectángulo se obtiene al multiplicar la base por la altura.

# def area_rectangulo(base, altura):
#     area  = base * altura
#     return area
# print(f'el area del rectangulo es: {area_rectangulo(15, 10)}')


#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo
# a partir de un radio. Calcula el área de un círculo de 5 de radio
# El área de un círculo se obtiene al elevar el radio a dos y 
# multiplicando el resultado por el número pi. 
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.


# pi = 3.14159    
# def area_circulo(pi, radio):
#     area = pi * (radio * radio)
#     return area
# print(f'el area del circulo es: {float(area_circulo(pi, 5))}')


#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

# def relacion(num1, num2):
#     if num1 > num2:
#         return 1
#     elif num1 < num2:
#         return -1
#     elif num1 == num2:
#             return 0


# print(relacion(5, 10))
# print(relacion(10, 5))
# print(relacion(5, 5))
       

# 4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

#  El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

# Comprueba el punto intermedio entre -12 y 24

# num1 = input('Ingrese su primer numero: ')
# num2 = input('Ingrese su segundo numero: ')


# def intermedio(num1, num2,):
#     num_intermedio = (num1 + num2) / 2
#     return num_intermedio

# print(f'el punto intermedio entre ambos numeros es:  {intermedio(-12, 24)}')




# 5) Realizá una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

# def recortar(num_recortar, limite_inf, limite_sup):
#     if num_recortar < limite_inf:
#         return 0
#     elif num_recortar > limite_sup:
#         return 10
#     else:
#         return num_recortar
# print(recortar(15, 0, 10))




# 6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares, y la segunda con los números impares:
# Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

#Por ejemplo:

# pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]


# lista_num = [6, 5, 2, 1, 7, 8, 10, 3, 0]
# pares = []
# impares = []
# def separar(lista):
#     for i in lista:
#         if i % 2 == 0:
#             pares.append(i)
#             pares.sort()
#         else:
#             impares.append(i)
#             impares.sort()
#     return pares, impares
# separar(lista_num)
# print(f'La lista de numeros pares es: {pares}')
# print(f'La lista de numeros impares es: {impares}')


