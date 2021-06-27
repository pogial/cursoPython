#Crear Lista
numeros = [1,58,3,5,4,7,95,15,24]

#Recorrer Lista
def mostrarLista(Lista):
    contador = 1
    for numero in Lista:
        print(f"El {contador} numero de la Lista es: {numero}")
        contador += 1

mostrarLista(numeros)

#Ordenar y Mostrar Lista
numeros.sort()
print(numeros)

#Mostrar Longitud
print(f"La longitud de la lista es: {len(numeros)}")

#Busquedad en la Lista
busquedad = int(input("Digita un numero? "))

comprobar = isinstance(busquedad, int)

while not comprobar or busquedad <= 0:
    busquedad = int(input("Digita un numero? "))
else:
    print(f"Has introducido: {busquedad}")

search = numeros.index(busquedad)
print(f"El numero buscado esta en el indice: {search}")