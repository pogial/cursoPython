#Capturar Excepciones y manejar errores

try:
    nombre = input("Cual es tu nombre? ")
    print(nombre)

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: "+ nombre
        
    print(nombre_usuario)
except:
    print("Error, Ingresa bien el nombre")
else:
    print("Todo funciona bien")
finally:
    print("Fin de la Iteracción")