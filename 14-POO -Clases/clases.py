#POO

#Definir una clase
class Coche:
    #Atributos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos = 500
    plazas = 2

    #Metodos
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.color = modelo
    def getModelo(self):
        return self.modelo
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad

#Instanciar la Clase
auto = Coche()

print(auto)
print(auto.marca)
print(auto.color)
print("La velocidad actual es: "+str(auto.getVelocidad()))
auto.acelerar()
print("La velocidad actual es: "+str(auto.getVelocidad()))