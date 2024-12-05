# Definición de los datos

## Origen de los datos

- [ ] Especificar la fuente de los datos y la forma en que se obtuvieron. 

El conjunto de datos fue recuperado del sitio huggingface (URL se muestra más abajo) 
y es un conjunto de imagenes de radiografías de tórax, este tipo de exámen es ampliamente utilizado 
en el diagnóstico de enfermedades pulmonares.

## Especificación de los scripts para la carga de datos

- [ ] Especificar los scripts utilizados para la carga de los datos. 

La carga de datos se realiza mediante los siguientes scripts:

/content/proyectoMLDS6/scripts/data_acquisition/carga_datos.py
/content/proyectoMLDS6/scripts/data_acquisition/carga_labels.py

## Referencias a rutas o bases de datos origen y destino.

- [ ] Especificar las rutas o bases de datos de origen y destino para los datos.

La referencia a los datos de origen se especifica en las siguientes URL:

https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset
https://nihcc.app.box.com/v/ChestXray-NIHCC


### Rutas de origen de datos

- [ ] Especificar la ubicación de los archivos de origen de los datos.

Los datos son descargados usando un escrip de python desde la siguientes URL´s:

https://nihcc.app.box.com/v/chestxray-nihcc
https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset/resolve/main/data

- [ ] Especificar la estructura de los archivos de origen de los datos.

La carpeta cargada contiene contiene 7121 elementos, cada uno correspondiente a imágenes 
diagnósticas en formato .png, en total tiene un peso de 2.8 GB equivalentes a 2800 MB. 
Todas corresponden a imágenes de rayos X de vista frontal de pacientes con posibles 
enfermedades torácicas.

El archivo .csv (data_Data_Entry_2017_v2020_ESTADO_SALUD) contiene las etiquetas correspondientes a cada imagen 
descargada del repositorio. Este archivo contiene dos colunmas: Image Index y Estado_Salud; la primera guarda información
del nombre de la imagen y la segunda guarda información de la etiqueta.

- [ ] Describir los procedimientos de transformación y limpieza de los datos

El objetivo de este análisis es la clasificación del estado de salud de un pacientes 
según su imagen diagnóstica, en la que es posible que sea identifacada alguna de las 8 patologias 
pulmonares más comunes o se determine que está sano. Para efectos practicos se construye un dataset 
para desarrollar un problema de clasificación binaria, no multiclase, siendo cero (0) para ausencia de alguna enfermedad
y uno (1) cuando se tiene la presencia de alguna patologia.

Como parte de la transformación de los datos se realizan las siguientes actividades:

1. Se hace un redimensionamiento de cada una de las imagenes para 
poder ser procesadas por el modelo seleccionado (ResNet): 224 píxeles de alto y 224 píxeles de ancho. 

2. Convertir las imagenes en tensores de PyTorch. 

3. Se normaliza los valores de los píxeles para alinearlos con las estadísticas esperadas por modelos preentrenados
como ResNet.

 
### Base de datos de destino

No hay un destino definido para los datos, solo se utilizan para el entrenamiento del modelo.
