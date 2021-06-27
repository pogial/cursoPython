texto = ""
print(texto)
if len(texto.strip()) <= 0:
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido: {texto}")