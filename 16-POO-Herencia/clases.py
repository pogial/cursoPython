class Persona:
    nombre = None
    apellidos = None
    altura = None
    edad = None

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy Hablando"

    def caminar(self):
        return "Estoy Caminando"

    def dormir(self):
        return "Estoy Durmiendo"

class Informatico(Persona):
    lenguajes = None
    experiencias = None

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencias = 5
    
    def getLenguajes(self):
        return self.lenguajes

    def getExperiencias(self):
        return self.experiencias

    def setLenguajes(self, lenguajes):
        self.lenguajes = lenguajes

    def setExperiencias(self, experiencias):
        self.experiencias = experiencias

    def programar(self):
        print("Estoy programando")