#Definir una clase
class Coche:
    #Atributos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos = 500

    #Constructor
    def __init__(self, color, marca, modelo, velocidad, caballos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballos = caballos

    #Metodos
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.color = modelo
    def getModelo(self):
        return self.modelo
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def setCaballos(self, caballos):
        self.caballos = caballos
    def getCaballos(self):
        return self.caballos
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad