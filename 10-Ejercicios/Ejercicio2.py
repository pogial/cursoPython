#Crear Lista
numeros = [1,2,8,4,62,32,37,48,159,254,15632,12,9,8,7,6,5,4]
print(numeros)

numero = int(input("Digite el numero adicionar en la lista? "))

def mostrarLista(Lista):
    for numero in Lista:
        print(numero)

if len(numeros) < 120:
    numeros.append(numero)
    mostrarLista(numeros)