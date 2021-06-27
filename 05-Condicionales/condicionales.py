#Condicionales
print("*************************EJEMPLO 1***************************")

color = input("Cual es tu color Favorito? ")

if color == "Azul":
    print("EEnhorabuena!!!")
    print("El color es Azul")
else:
    print("El color no es Azul")

print("*************************EJEMPLO 2***************************")
numero1 = input("Digita un primer Numero? ")
numero2 = input("Digita un segundo Numero? ")

if numero1>numero2:
    print("El "+str(numero1)+" es mayor a "+str(numero2))
if numero1<numero2:
    print("El "+str(numero1)+" es menor a "+str(numero2))

if numero1==numero2:
    print("El "+str(numero1)+" es igual a "+str(numero2))
else:
    print("El "+str(numero1)+" no es igual a "+str(numero2))

print("*************************EJEMPLO 3***************************")
nombre = input("Cual es tu nombre? ")
pais = input("Pais donde naciste? ")
edad = input("Cuantos años tienes? ")
mayoria_edad = 18

if int(edad) >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if pais == "Colombia":
        print("El usuario es Colombiano")
    else:
        print("El usuario no es Colombiano")    

else:
    print(f"{nombre} no es mayor de edad")

print("*************************EJEMPLO 4***************************")
dia = input("Que día de la semana en numero es hoy? ")

if int(dia) == 1:
    print("Hoy es Lunes")
elif int(dia) == 2:
    print("Hoy es Martes")
elif int(dia) == 3:
    print("Hoy es Miercoles")
elif int(dia) == 4:
    print("Hoy es Jueves")
elif int(dia) == 5:
    print("Hoy es Viernes")
elif int(dia) == 6:
    print("Hoy es Sabado")
elif int(dia) == 7:
    print("Hoy es Domingo")
else:
    print("El numero no corresponde a un día de la semana")

print("*************************EJEMPLO 5***************************")
edad_minima = 18
edad_maxima = 65
edad_oficial = input("Cuantos años tienes? ")

if int(edad_oficial) >= int(edad_minima) and int(edad_oficial) <= int(edad_maxima):
    print("La persona esta en edad para trabajar")
else:
    print("La persona no esta en edad de trabajar")