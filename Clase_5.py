#ser
#lista1 = [1,2,3,4,5, 'string', ('uno', 'dos')]
#tupla1 = (1,2,3,4,5, 'string', ['uno', 'dos'])
#set1 = {1,2,3,4,5, ('uno', 'dos'), 'string'}

#print(lista1)
#print(tupla1)
#print(set1)

#a_tupla = tuple(lista1)
#a_set = set(a_tupla)
#a_lista = list(a_set)

#print(a_lista)
#print(a_tupla)
#print(a_set)

#print(set(range(4, 15)))

#metodo add
#set1 = {1,2,3,4,1 'string', ('uno', 'dos')}
#print(set1)
#set1.add('un nuevo vaor')
#print(set1)

#metodo update

#set1.update([123, 'primer valor'])
#set1.update((12, 'segundo valor'))
#set1.update(range(24,36))
#set1.update(('valor unico',))
#set1.update('valor unico')

#print(set1)

#funcion len

#print(len(set1))

#metodo discard

#set1.discard('string')
#print(set1)

#metodo remove

#set1.remove(('uno', 'dos'))
#print(set1)

#operador in

#resultado = 6 in set1
#if 1 in set1:
 #   print(true)
#if 'uno' in set1:
 #   print('pase por aca')    
#print(resultado)

#metodo clear

#set1.clear()
#set1 = set()
#print(set1)

#metodo pop

#lista1 = [1,2,3,4]
#valor = lista1.pop(2)
#print(valor)
#print(lista1)

#valor = set1.pop()
#print(valor)
#print(set1)

#ejercicio
#grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
#añade los nombre: Ana, Ramón, Marta, Eric, David
#quita los nombre : Mario, Miguel, Esteban


#grupo = {'miguel', 'blanca', 'mario', 'andres'}

#grupo.add(('ana', 'ramon', 'marta', 'eric', 'david'))
#grupo1 = grupo
#print(grupo1)

#grupo.remove(('mario'))
#grupo.remove(('miguel'))
#grupo.remove(('esteban'))

#grupo2 = grupo1
#print(grupo2)

#diccionarios

#lista1 = []
#tupla1 = ()
# set1 = set()
#dicc = {}

#lista1 = [1,2,3,4,5]
#lista1[2]

#dicc = {
 #   'llave': 'valor',
  #  4: 'valor2',
   # 'llave2' : True,
#}

auto = {
    'patente':1525,
    'color':'rojo',
    'ruedas':4,
    'motor': 'v8',
    'puertas':2
}

#print(auto['motor'])
#print(auto['patente'])

#auto['color']= 'verde'
#print(auto['color'])

#auto['puertas'] += 2
#print(auto['puertas'])


#metodo update

auto.update({'motor': 'v12', 'seguro': True})
print(auto)

#funcion len

print(len(auto))

#funcion del

del auto['motor']
print(auto)

#funcion del


#operador in

print('verde' in auto)
print('seguro' in auto)

#metodo clear

auto.clear()
auto = {}
print(auto)

#metodo pop

valor = auto.pop('puertas')
print(valor)
print(auto)

valor = auto.pop('pepito', 'esta llave no se encuentra en el dicc de auto')
print(valor)
print(auto)

 #Programa las siguientes instrucciones de forma ordenada sobre la variable animales:

# Añade al diccionario las claves perro, tigre y mono con sus respectivos valores dog, tiger y monkey
# Modificá las claves elefante y delfin con los valores elephant y dolphin respectivamente
# Por último elimina del dict las claves dolphin y cat

# animales = {"elefante": "", "delfin": ""}

animales = {'elefante': '', 'delfin', ''}
print(animales)
animales.update({'perro': 'dog', 'tigre': 'tiger', 'mono': 'monkey'})
print(animales)
animales.update((('delfin', 'dolphin'),))
animales['elefante']= 'elephant'
print(animales)
del animales['delfin']
animales.pop('cat', '')
print(animales)
