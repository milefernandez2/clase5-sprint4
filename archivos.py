# #Para abrir un archivo:
# """ 
# f = open('textos/hola.txt',"w")
# #La función open recibe como parámetros el nombre y ubicación del archivo; y el modo en el que se quiere abriir el archivo
# #Modos:
# # 'r' (abrir para leer), 'w' (abrir para escribirlo), 'x', 'a' (append), 't', 'b', '+'
# f.write("Ya es hora")
# f.write("de cerrar el archivo") #la función write reemplaza el texto original por lo que pongamos
#  """
# f = open('textos/hola.txt',"a")
# f.write("\n Ahora agrego texto")

# #Cuando se termina de procesar un archivo se debe cerrarlo para liberar el recurso de memoria
# f.close()

# f = open('textos/hola.txt',"r")
# # text = f.read() #Para leer el texto. Lee el archivo completo. Para los casos en que los archivos son muy grandes se generalmente se lee linea por linea para no ocupar tanta memoria
# # print(text)

# #Podemos especificar el tamaño que queremos leer:
# text = f.read(8) 
# print(text)

#Hacemos una función que copie de un archivo a otro:

def copiaArchivo(oldFile, newFile):
    f1 = open(oldFile, 'r')
    f2 = open(newFile, 'w')
    while True:
        texto = f1.read(50) #se lee de a 50 caracteres
        if texto == "":
            break
        f2.write(texto)
    f1.close()
    f2.close()

copiaArchivo('textos/hola.txt', 'textos/hola2.txt')
