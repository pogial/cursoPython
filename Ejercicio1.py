"""
Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
    * Recorrer la lista y mostrarla.
    * Hacer funcion que recorra lista de numeros.
    * Ordenarla y mostrarla.
    * Mostrar su longitud.
    * Buscar algun elemento digitado por el usuario.
"""

#Hacer funcion que recorra la lista
def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado = "Elemento: " + str(elemento)
        print(resultado)

#Crear Lista
numerosLista = [13,64,52,73,21,7,91,63]

#Recorrer y mostrar
print("*********RECORRER Y MOSTRAR***********")
mostrarLista(numerosLista)

#Ordenar y mostrar
print("*********ORDENAR Y MOSTRAR************")
numerosLista.sort()
mostrarLista(numerosLista)

#Mostrar su longitd
print("*********LONGITUD*********************")
print("Logitud de la Lista es: " + str(len(numerosLista)))