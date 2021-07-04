#Excepciones Personalizadas
try:
    nombre = input("Digita el nombre ")
    edad = int(input("Digita la edad "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al curso de Python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Error: ", e)