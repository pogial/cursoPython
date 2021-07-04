#Multiples Excepciones

try:
    numero = int(input("Digita un numero "))
    print("El cuadrado del numero es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros")
except ValueError:
    print("Debes digitar un numero")
except Exception as e:
    print("Error: ", type(e).__name__)