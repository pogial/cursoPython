from io import open
import pathlib
import shutil
import os

#Abrir Archivo
ruta = str(pathlib.Path().absolute())+"/archivo_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

#Escribir en el Archivo
#archivo.write("***********Este es el curso de Python***********\n")

#Cerrar Archivo
archivo.close()

#Leer Archivo y leer Contenido
ruta = str(pathlib.Path().absolute())+"/archivo_texto.txt"
archivo_lectura = open(ruta, "r")

#contenido = archivo_lectura.read()

#print(contenido)

#for elemento in contenido:
#    print(elemento)

#Leer Contenido y Guardarlo en Lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)

for linea in lista:
    print(linea.upper())

#Copiar Archivo
ruta_original = str(pathlib.Path().absolute())+"/archivo_texto.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/archivo_texto_copia.txt"
shutil.copyfile(ruta_original,ruta_nueva)

#Mover Archivo
ruta_original = str(pathlib.Path().absolute())+"/archivo_texto.txt"
ruta_nueva = str(pathlib.Path().absolute())+"\Mover-Archivos/archivo_texto_movido.txt"
print(ruta_nueva)
shutil.move(ruta_original,ruta_nueva)

#Eliminar Archivo
ruta_original = str(pathlib.Path().absolute())+"/archivo_texto_copia.txt"
os.remove(ruta_original)