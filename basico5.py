# pip install pandas openpyxl
# pip install -r .\requirements.txt
import pandas as pd

# Datagrame es la informacion basica con el nombre de las piezas y centimetros para poder armar el excel

data = {
    "Piezas:":["Pata","Tablero","Puerta","Estante","Panel","Panel Lateral"],
    "Centimetros":[50,20,30,180,30,40]
}

df = pd.DataFrame(data)

# guardar el dataframe en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)
