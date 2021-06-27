print("*******************************EJEMPLO 1*********************************")
pelicula = "Batman"
print(pelicula)

peliculas = ["Batman","Robin","Gatubela"]

for pelicula in peliculas:
    print(pelicula)

otrasPeliculas = list(("Superman","Acuaman","Mujer Maravilla"))
print(otrasPeliculas)
print(otrasPeliculas[-1])


numeros = list(range(2020,2051))
print(numeros)
print(numeros[0:4])
print(numeros[2:4])

variado = ["Alex", 30, 4.4, True, "Hola"]
print(variado)
variado.append("Luis")
print(variado)

print("*******************************EJEMPLO 2*********************************")
contactos = [
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'Alex',
        'alex@gmail.com'
    ],
    [
        'Jorge',
        'jorge@hotmail.com'
    ]
]

print(contactos[2][1])

for contacto in contactos:
    print(contacto)