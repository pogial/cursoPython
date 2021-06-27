print("******************************EJEMPLO 1*********************************")

def muestraNombres():
    print("Alex")
    print("Paco")
    print("Hugo")
    print("Luis")
    print("Nestor")
    print("\n")

muestraNombres()    

print("******************************EJEMPLO 2*********************************")

def muestraTuNombre(nombre, edad):
    print("Tu nombre es: "+nombre+" y tienes "+str(edad)+" años")

nombre = input("cual es tu nombre? ")
edad = input("Cual es tu edad? ")

muestraTuNombre(nombre,edad)

print("******************************EJEMPLO 3*********************************")
def muestraTuNombre(nombre, edad = None):
    print("Tu nombre es: "+nombre+" y tienes "+str(edad)+" años")

nombre = "Alex"
edad = 30

muestraTuNombre(nombre)

print("******************************EJEMPLO 4*********************************")
def RetornaNumero(numero):
    print("El numero es: "+str(numero))
    if numero > 10:
        return "El numero es mayor a 10"
    else:
        return "El numero es menor a 10"

numero = input("Digita un numero? ")

texto = RetornaNumero(int(numero))

print(texto)

print("******************************EJEMPLO 5*********************************")
dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))