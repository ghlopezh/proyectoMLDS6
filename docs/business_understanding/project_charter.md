# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Diagnostico de enfermedades respiratorias por emdio de machine learning utlizado imagenes de radiologia simple

## Objetivo del Proyecto

En colombia, las infecciones respiratorias son consideradas la quinta causa de mortalidad, las imágenes diagnósticas, en especial los raxos x a nivel de la cavidad toráxica constituyen una herramienta común, económica y accesible en la mayoría de los casos para la detección y seguimiento de este tipo de enfermedades, de tal manera que su adecuado entendimiento y análisis  puede marcar una gran diferencia en la evolución de los pacientes,  en este contexto,  metodologías como el deep learning puede contribuir para un mejor entendimiento y aprovechamiento de estos exámenes clínicos.

## Alcance del Proyecto

Dada la naturaleza de los datos, se propone construir y entrenar una red neuronal que permita tomar una imagen diagnóstica en formato png se pueda realizar una evaluación del contenido de la imagen y retornar un posible diágnostico de enfermedad o considerar a un paciente como sano. Estos resultados pueden generar valor para la enseñanza de casos clínicos de imaginología en el internado médico.

### Incluye:

- Descripción de los datos disponibles

Provide a link to the NIH download site: https://nihcc.app.box.com/v/ChestXray-NIHCC
Include a citation to the CVPR 2017 paper (see Citation information section)
Acknowledge that the NIH Clinical Center is the data provider

Citation Information

@inproceedings{Wang_2017,
    doi = {10.1109/cvpr.2017.369},
    url = {https://doi.org/10.1109%2Fcvpr.2017.369},
    year = 2017,
    month = {jul},
    publisher = {{IEEE}
},
    author = {Xiaosong Wang and Yifan Peng and Le Lu and Zhiyong Lu and Mohammadhadi Bagheri and Ronald M. Summers},
    title = {{ChestX}-Ray8: Hospital-Scale Chest X-Ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases},
    booktitle = {2017 {IEEE} Conference on Computer Vision and Pattern Recognition ({CVPR})}
}

- [Descripción de los resultados esperados]

The text-mined disease labels are expected to have accuracy >90%.Please find more details and benchmark performance of trained models based on 14 disease labels in our arxiv paper: 1705.02315

- [Criterios de éxito del proyecto]



### Excluye:

- Se excluye del proyecto:
- Puesta en producción para fines comerciales
- La disposición de API para consumo de aplicaciones dado los datos confidenciales y los resultados de los pacientes
- Utilzacion de datos de origen confidencial

## Metodología

Fase 1: Definición del Problema de Negocio

	•	Problema: Crear un modelo basado en ResNet50 para clasificar imágenes de rayos X del tórax y detectar enfermedades como neumonía o enfisema.
	•	Objetivo: Mejorar la precisión del diagnóstico automatizado.
	•	Métricas de éxito:
	•	Precisión (Accuracy).
	•	Sensibilidad (Recall) y especificidad.
	•	Área bajo la curva ROC (AUC-ROC).
	•	Integración con Herramientas:
	•	Usar GitHub para versionar el código del proyecto.
	•	Configurar DVC para versionar los datos del dataset NIH y facilitar la reproducibilidad.
	•	Definir un flujo de experimentación con MLflow para registrar hiperparámetros, métricas y versiones del modelo.

Fase 2: Adquisición y Comprensión de los Datos

	•	Actividades:
	1.	Descargar el dataset desde Hugging Face.
	2.	Analizar y limpiar los datos (calidad, clases desbalanceadas, imágenes corruptas).
	3.	Dividir los datos en conjuntos de entrenamiento, validación y prueba (70/15/15).
	4.	Subir los datos crudos al repositorio GitHub (o a un almacenamiento externo) y versionarlos con DVC:
	•	Inicializar un repositorio con dvc init.
	•	Rastrear los datos con dvc add.
	•	Subir los datos a un almacenamiento remoto (como S3 o Google Drive).
	•	Resultado:
	•	Datos versionados y reproducibles.
	•	Historial de cambios en los datos gestionado por DVC.

Fase 3: Modelado

	•	Actividades:
	1.	Preprocesamiento:
	•	Normalizar imágenes y aplicar data augmentation (rotación, escalado, etc.).
	•	Configurar pipelines con DVC para etapas como preprocesamiento, entrenamiento y evaluación.
	2.	Entrenamiento del Modelo:
	•	Usar ResNet50 preentrenada y adaptar la última capa para las clases del dataset.
	•	Registrar los experimentos con MLflow:
	•	Guardar hiperparámetros como learning rate, batch size, y número de épocas.
	•	Registrar métricas como precisión, pérdida, y AUC.
	•	Usar DVC para rastrear los modelos generados y los resultados intermedios.
	3.	Validación y Comparación de Experimentos:
	•	Analizar métricas en MLflow para identificar las mejores configuraciones.
	•	Guardar el mejor modelo en MLflow para su despliegue posterior.

Fase 4: Implementación

	•	Actividades:
	1.	Convertir el modelo final a un formato optimizado (como ONNX o TensorFlow Lite).
	2.	Desplegar el modelo utilizando un servidor de predicciones, como FastAPI o Flask.
	3.	Usar MLflow para gestionar el despliegue del modelo:
	•	Registrar el modelo como parte de MLflow Model Registry.
	•	Configurar un entorno de producción y pruebas para el modelo.
	4.	Documentar el proceso de despliegue y subir el código a GitHub.

Fase 5: Supervisión y Mantenimiento

	•	Actividades:
	1.	Monitorear el rendimiento del modelo en producción, usando métricas como precisión y tasa de error.
	2.	Versionar nuevos conjuntos de datos con DVC cuando se disponga de imágenes actualizadas.
	3.	Iterar sobre nuevos experimentos registrados con MLflow para mejorar continuamente el modelo.
	4.	Realizar revisiones periódicas del código y la documentación en GitHub, y mantener issues o pull requests para gestionar colaboraciones.

Flujo de Herramientas:

	1.	GitHub:
	•	Control de versiones del código y scripts del proyecto.
	•	Documentación del proyecto en el repositorio.
	2.	DVC:
	•	Versionamiento de los datos (dataset y modelos entrenados).
	•	Gestión de pipelines reproducibles.
	3.	MLflow:
	•	Registro de experimentos, métricas, y parámetros del modelo.
	•	Gestión y despliegue del modelo en producción.


## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 15 al 21 de noviembre|
| Preprocesamiento, análisis exploratorio | 1 semanas | del 22 al 29 de noviembre|
| Modelamiento y extracción de características | 1 semanas | 30 de noviembre al 6 de diciembre|
| Despliegue | 1 semanas | del 7 al 14 de diciembre |
| Evaluación y entrega final | 1 semanas | del 15 al 21 de diciembre |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- Lider del proyecto: Olga lizeth castellanos Galeano Rol: Data scientist
- Wilson Rojas Lider Rol: Arquitectura Rol: MLOps
- Giovanny Lopez Herazo Rol: Lider de Infraestructura 

## Presupuesto

Recursos Propios y recursos de la UNAL a nivel de conocimiento y tecnico

## Stakeholders

- Msc Oscar Alberto Bustos Cooordinador Proyecto Aplicado
- Evaluador de la propuesta de proyecto aplicado
- Expectativa; Aplicar correctamente las metodoogia Agile en machine learning

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
