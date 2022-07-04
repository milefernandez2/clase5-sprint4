#Listas (se representan con corchetes)
from operator import index


dias = ["lunes", "martes", "miercoles", "jueves", "viernes"] #lista de strings
numeros = [7, 14, 21] #lista de números
listaVacia = [] #la lista vacía se representa con los corchetes solos
listaCompuesta = ["hola", 2.0, 5, [10, 20, 30, 40, 50]] #lista formada por diferentes tipos: string, float, int, lista de enteros
print(dias) #imprime todos los dias
print(dias[2]) #imprime miercoles

#Las listas se pueden modificar
dias[1] = "tuesday"
print(dias)
print(dias[-1]) #Podemos acceder a las listas con indices negativos. El -1 representa el último elemento de la lista (viernes)

print(numeros)
print(numeros[1])
print(numeros[3-2]) #resuelve primero 3-2, por lo que imprime numeros[1]

print(listaCompuesta)
print(listaCompuesta[3]) #imprime la lista de números enteros que está dentro de la lista compuesta
print(listaCompuesta[3][1]) #imprime el "20" que está dentro de la lista de números enteros


#Range
#generamos una lista de números a partir del range
listaNumeros1 = list(range(2, 6)) #"list" es el constructor de la lista
print(listaNumeros1) #se genera una lista de números que van del 2 al 5
listaNumeros2 = list(range(10))
print(listaNumeros2) #se asume que el start = 0 y se genera una lista del 0 al 9
listaNumeros3 = list(range(1, 10, 2)) #dentro del range tenemos start, finish y step
print(listaNumeros3) #imprime 1,3,5,7,9: va del 1 al 10 en pasos de 2

#FORMAS DE RECORRER UNA LISTA
#While
i = 0
while i <= len(listaNumeros1):
    print(dias[i])
    i += 1
print("--------")

#For in
for dia in dias:
    print(dia)
print("--------")

#For range
for i in range(len(dias)):  #equivale a for i in range(0, len(dias)): --> omito el start
    print(dias[i])


#Evaluamos la pertenencia de un miembro a una lista:
if "tuesday" in dias: #preguntamos si un elemento está presente en una lista
    print("lo encontré")

#Operaciones de las listas:
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #La suma también funciona con elementos de tipo lista: se concatenan las listas
print(c)
print(a * 3) #se repite 3 veces la lista a


#Slicing
lista = ["a", "b", "c", "d", "e", "f"]
#         0    1    2    3    4    5
print(lista[1:3]) #imprime b y c
print(lista[:4]) # imprime a, b, c y d
print(lista[3:]) # imprime d, e y f
print(lista[:]) # imprime la lista completa


#Para eliminar elementos de la lista:
del(lista[1]) #se elimina b
print(lista)


#Clonar lista
listaClonada = []
listaClonada[:] = lista[:]
print(listaClonada)

#Agregar lista
listaAgregada = [1, 3, 5]
listaAgregada[3:] = lista[:]
print(listaAgregada)

#Las listas se pueden usar como pilas o como colas

#Pilas
#Funcionan bajo el principio de LIFO (Last In First Out): el último en entrar es el primero en salir
lista = ["a", "b", "c", "d", "e", "f"]

lista.append("g") #append agrega un elemento al final de la lista
lista.append("h")
lista.append("i") 
print(lista) 

lista.pop() #pop elimina el último elemento de la lista
print(lista)

#Insertar un valor en una posición determinada:
lista.insert(2,"ch") #la función insert recibe el índice y el objeto: en la posición 2 inserta "ch"
print(lista)

#Eliminar un valor determinado:
lista.remove("ch") #si hay más de 1 "ch" en la lista remueve solo el primero
print(lista)

#Para averiguar el índice de un elemento:
print(lista.index("d"))  
print("-----")

numerosDesordenados = [8, 1, 6, 9]
print(sorted(numerosDesordenados)) #sorted ordena los números

print(sorted(numerosDesordenados, reverse=True)) #reverse es un Named parameter

def imprimirLista(reverse=False,list=[]): #la función imprimirLista recibe 2 parámetros: reverse y list. a los parámetros les seteo un valor por defecto
    if reverse: #(si reverse es True)
        for i in reversed(range(0, len(list))):
            print(list[i])
    else:
        for elem in list:
            print(elem)

imprimirLista(list = [1, 5, 6, 7]) #como no le paso el reverse como parámetro, se asume el valor por defecto establecido que era False
print("-----")
imprimirLista(list = [1, 5, 6, 7], reverse=True) #los Named parameter me permiten pasar los parámetros desordenados porque justamente los parámetros tienen nombre
print("-----")
imprimirLista(True, [1, 19, 20]) #si no pongo los nombres de los parámetros tengo que respetar el orden


