import pandas as pd

df = pd.read_excel("./prueba.xlsx")


def calcular_renta(fila):
    renta = fila["Sueldo Base Mensual $"] + fila["Gratificación Mensual $"] + fila["Asignación Almuerzo Mensual $"] + \
        fila["Vales Almuerzo Valor Bruto Mensual $"] + \
        fila["Valor Casino  Bruto Mensual $"] + \
        fila["Asignación Movilización Mensual $"]

    return renta


df["Renta Bruta"] = df.apply(calcular_renta, axis=1)

df.to_excel("prueba_con_renta_bruta.xlsx", index=False, header=True)