# Ejercicio Nro 1

# Escribi un programa que lea los dos numeros por teclado y permita elegir entre 4 opciones en un menu:
# 1) mostrar una suma de los dos numeros
# 2) Mostrar una resta de los dos numero (el primero menos el segundo)
# 3) Mostrar una multiplicacion de los dos numeros
# 4) Si elige esta opcion se interrumpira la impresion del menu y el programa finalizara
# 5) En caso de no introducir una opcion valida, el programa informara de que no es correcta


# num1 = int(input('ingrese un numero: '))
# num2 = int(input('ingrese otro numero: '))

# print('''\nopciones del menu:\n 
#     1. mostrar una suma entre los dos numeros\n 
#     2. mostrar una resta de los dos numeros (el primero menos el segundo) \n
#     3. mostrar una multiplicacion entre los numeros\n
#     4. se interrumpira el menu y el programa finalizara \n''')


# suma = num1 + num2
# resta = num1 - num2 
# multiplicacion = num1 * num2

# menu = int(input('ingrese una opcion: '))
# while menu < 1 or menu > 4: ##esta es la condicion para seguir pidiendo numeros en caso de que se coloque una opcion no valida
#     print('numero no valido')
#     menu = int(input('ingrese una opcion: '))

# if menu == 1:
#     print(suma)
# elif menu == 2:
#     print(resta)
# elif menu == 3:
#     print(multiplicacion)
# while menu == 4: 
#     print('finalizando programa')
#     break 




# ejercicio 2)
# Escribe un progrrama que lea un numero impar por teclado. 
# si el usuario no introduce un numero impar, 
# debe repetirse el proceso hasta que lo introduzca correctamente.                  



# valor = int(input('ingrese un numero: '))

# while (valor % 2) == 0:
#     valor = int(input('ingrese un numero: '))
#     if (valor % 2) != 0:
#           print('su numero es correcto')      
#     break     




# ejercicio 3)
# Escribi un programa que sume todos los numeros enteros impares desde el 0 hasta el 100:
# podes utilizar la funcion sum y range
# el tercer parametro de la funcion  range (inicio, fin, salto) indica un salto de numeros

# suma = 0
# for numero in range(1, 101, 2):
#     suma = suma + numero
#     print(suma)

# suma = sum(list(range(1,101,2)))
# print(suma)




#Ejercicio 4)
#Escribi un programa que pida al usuario cuantos numeros quiere introducir
#luego de todos los nummeros y realiza una media aritmetica


# respuesta = "si"
# valoresIngresados = []

# while respuesta == "si":
#     numeroIngresado = int(input('ingresa el número que quieras: '))
#     valoresIngresados.append(numeroIngresado)
#     respuesta = input('¿quiere ingresar mas numeros? si para continuar: ')

# print(
#     f'Los numeros ingresados fueron {valoresIngresados}, y la media de todos los ingresos sumados es: {sum(valoresIngresados)/len(valoresIngresados)} ')






#Ejercicio 5)
#Escribi un programa que pida al usuario un numero entero del 0 al 9,
#y que mientras el numero no sea correcto se repita el proceso
#luego debe comprobarse si el nuero se encuentra en la lista de numeros y notificarlo:

# numeros = [1, 3, 6, 9]

# n_entero = int(input('ingrece un numero entero del 0 al 9: '))
# while not n_entero in range(0, 10):
#     n_entero = int(input('incorrecto, ingrese otro numero: '))
# else: print('respuesta correcta')

# if n_entero in numeros:
#     print('se encuentra en la lista')
# else: print('no se enceuntra en la lista')




#Ejercicio 6)
#utilizando la funcion range() y la conversiona alista
#genera las siguientes listas dinamicamente:

#todos los numeros del 0 al 10[0,1,2,...,10]

#todos los numeros del -10 al 0

#todso los numeros pares del 0 al 20

#todos los numeros impares entre -20 y 0

#todos los numeros multiples de 5 del 0 al 50 [0,5,10,...,50]

#tip: la conversion de listas es mi_lista=list(range(inicio,fin,sallto))


# lista_1 = []
# for xlista in range(0,11):
#     lista_1.append(xlista)
# print(lista_1)

# lista_2 = []
# for xlista in range(-10, 1):
#     lista_2.append(xlista)
# print(lista_2)

# lista_3 = []
# for xlista in range(0, 21, 2):
#     lista_3.append(xlista)
# print(lista_3)

# lista_4 = []
# for xlista in range(-19, 1, 2):
#     lista_4.append(xlista)
# print(lista_4)

# lista_5 = []
# for xlista in range(0, 55, 5):
#     lista_5.append(xlista)
# print(lista_5)             

# lista_1 = list(range(0,11))
# print(lista_1)

# lista_2 = list(range(-10,1,1))
# print(lista_2)

# lista_3 = list(range(0, 21, 2))
# print(lista_3)

# lista_4 = list(range(-20, 1, 2))
# print(lista_4)

# lista_5 = list(range(0, 51, 5))
# print(lista_5)  



#Ejercicio 7)
#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan ene ellas,
#pero no debe repetirse ningun elemento en la nueva lista:


lista_1 = ['h','o','l','a',' ','m','u','n','d','o']
lista_2 = ['h','o','l','a',' ','l','u','n','a']
lista_3 = []

for x in lista_1:
    for y in lista_2:
        if (x==y) and x not in lista_3:
            lista_3.append(x)
print(lista_3)
