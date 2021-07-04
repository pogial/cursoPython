import clases

persona = clases.Persona()
persona.setNombre("Alex")
persona.setApellidos("Giraldo Poveda")
persona.setEdad("43")
persona.setAltura("170")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Garcia Perez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.programar())
print(f"El informatico sabe programar en: {informatico.getLenguajes()}")