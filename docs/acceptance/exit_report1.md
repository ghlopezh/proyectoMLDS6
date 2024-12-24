# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

- Se realizó un versionamiento del modelo en DVC y se creo Interface por línea de comandos (CLI) para interactuar con el modelo desplegado con Mlflow.
- Los logros alcanzados son: mejoras en el versionamiento de los datos con  DVC; se realiza despliegue del modelo en Mlflow midiendo su confianza, que finalmente alcanza el 42%.
- La evaluación del modelo final no se comparo con el modelo base ResNet50.
- Los resultados obtenidos son: un nivel de confianza bajo. El esfuerzo principal se centro en el despliegue del modelo, la creación de la interface de usuario (CLI) y en el versionamiento de los datos de entrenamiento y el modelo.

## Lecciones aprendidas

- Los principales desafíos encontrados son: dado el tamaño del modelo se encontró dificultad en su despliegue. Otro desafío fue el trabajo con imágenes, dado que los ejemplos estaban enfocados en el manejo de texto.
- Las principales lecciones aprendidas en relación al modelo fue su tamaño y la dificultad para su manejo con los frameworks propuestos en el curso. El enfoque se realizó en el entrenamiento del modelo, dada la dificultad con el manejo de imágenes y su volumen; no nos centramos en la búsqueda de mejores hiper parámetros que hicieran mas eficiente el modelo.
- Es fundamental tener una estructura de trabajo definida desde el inicio de los proyectos de ML, además de definir una metodología clara para ejecutar los desarrollos y tareas propias del proyecto (despliegue, versionamiento, integración, entre otras) para garantizar su replicabilidad y facilitar el trabajo en equipo.

## Impacto del proyecto

- Un impacto del modelo es su uso como herramienta de apoyo para el personal medico a la hora de diagnosticar enfermedades. Sin embargo se podría mejorar las características del modelo, haciendo mas ligero y mas integrable en proyectos de ML con estas características.

Otro elemento de mejora es el uso de herramientas para el despliegue en ambientes web, que hagan que la experiencia del usuario sea más simple.

## Conclusiones

El modelamiento con datos reales supone un reto adicional dentro del proceso de aprendizaje de nuevas herramientas analíticas. 

Para proyectos futuros con análisis de imágenes se requiere considerar que el  uso de recursos físicos (GPU) esta limitado a las políticas de Google lo que supone un incremento en los tiempos de entrenamiento y procesamiento. Además, seria valioso contar con mas material de apoyo especifico para estos proyectos y un desarrollo desde el inicio del curso en paralelo con proyectos menos complejos como el análisis  de texto. 


## Agradecimientos

Agradecemos al equipo docente y su personal de apoyo, a la Universidad Nacional de Colombia por crear estos espacios de aprendizaje enfocados en en el hacer ligado con la teoría que resultan muy valiosos en la vida laboral.
