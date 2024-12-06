# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

En esta sección se presenta un resumen general de los datos. Se describe el número total de observaciones, variables, 
el tipo de variables, la presencia de valores faltantes y la distribución de las variables.

## Resumen de calidad de los datos

Por tratarse de datos descargados de repositorios especializados para el entrenamiento y modelado como 
huggingface.co, los datos descargados no registran valores faltantes, no se encuentran errores ni datos duplicados. 


## Variable objetivo.

La variable objetivo es "Estado_Salud" la cual tiene las etiquetas de cada imagen y que corresponden con si se encontraron patologías (1) o no (0).

En la siguiente imagen se puede evidenciar la distribución de la variable objetivo y se concluye que las clases tienen un balance aceptable (54% y 46%), 
por lo tanto no se utilizan tecnicas de revalanceo.

![Distribución variable objetivo](data_distribution.png)

| Variable | Conteo | Porcentaje |
| --- | --- | --- |
| 0.0 |	60361 | 54% |
| 1.0 |	51759 | 46$	|

## Variables individuales

En el data set usado no se utilizan otras variables. Básicamante, los datos utilizados constan de una imagen con su correspondiente etiqueta 
que la clasifica en dos categorias: presencia de patologias (1) o sin presencia de patologias (0) 

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan
técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

Esta sección no aplica, como ya se explico en el párrafo anterior.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la 
variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de 
dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la 
regresión lineal para modelar la relación entre las variables.

Esta sección no aplica, como ya se explico en el párrafo anterior.

