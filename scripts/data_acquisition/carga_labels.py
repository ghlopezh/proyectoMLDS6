import pandas as pd
from pandas import read_csv


csv_path = '/content/proyectoMLDS6/docs/data/data_Data_Entry_2017_v2020_ESTADO_SALUD.csv'
df = pd.read_csv(csv_path, sep=';')
# Separar el conjunto de datos entre entrenamiento y prueba
#train_df = df[df['Image Index'].isin([os.path.basename(path) for path in train_files])]
#test_df = df[df['Image Index'].isin([os.path.basename(path) for path in test_files])]

print(df.head())