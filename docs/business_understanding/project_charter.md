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

- [Descripción de lo que no está incluido en el proyecto]

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 1 de mayo al 15 de mayo |
| Preprocesamiento, análisis exploratorio | 4 semanas | del 16 de mayo al 15 de junio |
| Modelamiento y extracción de características | 4 semanas | del 16 de junio al 15 de julio |
| Despliegue | 2 semanas | del 16 de julio al 31 de julio |
| Evaluación y entrega final | 3 semanas | del 1 de agosto al 21 de agosto |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- [Nombre y cargo del líder del proyecto]
- [Nombre y cargo de los miembros del equipo]

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
