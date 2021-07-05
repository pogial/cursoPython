import mysql.connector

#conexion
database = mysql.connector.connect(
    host        = "localhost",
    user        = "root",
    passwd      = "",
    database    = "curso_python"
)

#Comprobar conexion
print(database)

#Crear Base de Datos
cursor = database.cursor()
"""cursor.execute("CREATE DATABASE IF NOT EXISTS curso_python")
cursor.execute("SHOW DATABASES")

#Listar Base de Datos
for bd in cursor:
    print(bd)"""

#Crear Tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")

cursor.execute("SHOW TABLES")

#Listar Tablas
for tb in cursor:
    print(tb)

#Insertar Registro en Tabla
"""cursor.execute("INSERT INTO vehiculos values (null,'Renault','Logan',4000)")
cursor.execute("INSERT INTO vehiculos values (null,'Mazda','mx-6',4000)")
cursor.execute("INSERT INTO vehiculos values (null,'Toyota','Pardo',24000)")
cursor.execute("INSERT INTO vehiculos values (null,'Renault','Duster',9000)")
database.commit()"""

#Leer datos de una Tabla
cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchall()

for coche in resultado:
    print(coche)