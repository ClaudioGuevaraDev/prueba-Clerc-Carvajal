import pandas as pd
import mysql.connector

# Conexión con mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Claudio123prueba",
    database="prueba"
)

mycursor = mydb.cursor()

# Leemos el excel con la renta bruta
df = pd.read_excel("../pregunta1/prueba_con_renta_bruta.xlsx")

# Iteramos el excel
for i in range(len(df)):
    # Cargamos los Cargos en MySQL
    nombre = df["Nombre del Cargo en la Empresa"].iloc[i]
    grado = df["Grado del Cargo según Evaluación Utilizada"].iloc[i]
    genero = df["Género (Masculino-Femenino)"].iloc[i]
    nacionalidad = df["Nacionalidad"].iloc[i]

    sql = "INSERT INTO Cargos (nombre, grado, genero, nacionalidad) VALUES (%s, %s, %s, %s)"
    val = (nombre, str(grado), genero, nacionalidad)
    mycursor.execute(sql, val)
    mydb.commit()

    # Cargamos las Rentas en MySQL
    cargo_insertado = mycursor.lastrowid
    renta_bruta = df["Renta Bruta"].iloc[i]

    sql = "INSERT INTO Rentas (cargo_id, renta_bruta) VALUES (%s, %s)"
    val = (cargo_insertado, int(renta_bruta))
    mycursor.execute(sql, val)
    mydb.commit()