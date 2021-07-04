from coche import Coche

carro = Coche("Gris","Renault","Logan",120,200)

print(carro.getColor())
print(carro.getMarca())
print(carro.getCaballos())
print(carro.getModelo())

#Detectar tipado
if type(carro) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un Objeto")