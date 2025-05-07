 
import pandas as pd

def cm_a_pulgadas(cm):
    return cm/2.54

# leer excel
df = pd.read_excel("muebles_medidas.xlsx")

# añadir columna al dataframe que sea de pulgadas y se rellene con el calculo de cm / 2354

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx",index=False)

print("Conversion completada y guardada en un nuevo archivo")

