import os

#Crear Carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

#Eliminar Carpeta
os.rmdir("./mi_carpeta")