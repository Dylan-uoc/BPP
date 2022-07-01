
import pandas as pd
import re
import matplotlib.pyplot as plt

df=pd.read_csv('finanzas2020[1].csv',  sep="\t")
df.head()

"""Con esta expresión regular quito los datos que no me permiten hacer la suma"""

suma_meses={}
for c in df:
    regex = re.compile(r'[^0-9]') # Eliminamos todo lo que no sean números
    df[c] = df[c].replace(regex, 0).astype(int)
    print(c)
    print(df[c].sum())
    print("\n")
    suma_meses[c]=df[c].sum()
print(suma_meses)

"""Ahora ya puedo sacar los meses de más ahorro y más gastos."""

max_gasto = min(suma_meses, key=suma_meses.get)
print(max_gasto)

max_ahorro = max(suma_meses, key=suma_meses.get)
print(max_ahorro)

"""Aquí saco el total de gastos en un año y la media de gastos."""

total_año = 0
total_ingresos = 0
total_gastos = 0
for key, value in suma_meses.items():
    total_año += value
    if value >=  0:
        total_ingresos += value
    else:
        total_gastos += value
        

print("el total de ingresos en un año es de ", str(total_ingresos)+"€")

print("El total de gastos en un año es de " + str(total_gastos)+ "€")

print("La media de gastos es: " + str(round(total_año/12,2)) + "€")

"""Gráfico de la evolución del gasto"""

plt.figure(figsize=(12,5))
plt.title("evolucion de gastos a lo largo del año")
plt.plot(suma_meses.keys(), suma_meses.values(), color='blue')
plt.show()

"""Apartado 2 de la actividad Haciendo uso de excepciones

Comprobando que el fichero existe
"""

try:
    with open('finanzas2020[1].csv', 'r') as f:
        print("El archivo existe")
except FileNotFoundError as e:
    print("El archivo no existe")

"""Cargamos de nuevo el documento para los siguientes puntos"""

df2=pd.read_csv('finanzas2020[1].csv',  sep="\t")

df2_columnas=[]
suma_meses={}
for c in df2:
    suma_meses[c]=df2[c].sum()
    df2_columnas.append(c)
print(df2_columnas)

class mesesError(Exception):
    pass

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
meses_df2 = len(df2.columns)
print(meses_df2)

"""Comprobando que tiene 12 columnas, una para cada mes del año"""

if meses_df2 != 12:
    raise mesesError("El número de columnas no es correcto")
else:
    print("El número de columnas es correcto")
    if ((df2_columnas) != meses):
        raise mesesError("El nombre de las columnas no es correcto")
    else:
        print("El nombre de las columnas es correcto")

"""Comprobando que tengan datos"""

class mesVacio(Exception):
    pass

for c in df2:
    if df2[c].sum() == 0:
        raise mesVacio("El mes " + c + " está vacio")
    else:
        print("El mes " + c + " no está vacio")

"""Comprobando que todos los datos son correctos. De no haber un dato correcto, el programa debería saber actuar en consecuencia y continuar con su ejecución pero no soy capaz de lograr este punto."""

class datoString(Exception):
    pass

for c, dato in df2.iterrows():
    for d in dato:
        if type(d) == str:
            raise datoString("El dato " + d + " es string")
        else:
            print("El dato " + d + " es numero")