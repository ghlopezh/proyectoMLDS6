# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** best_model.h5-2.keras
- **Plataforma de despliegue:** El despliegue se realiza mediante FastApi y la plataforma Railway.
- **Requisitos técnicos:**   El modelo y su arquitectura para el despliegue requieren python 3 o superior, con las librerías específicadas en el archivo Requirements.txt en la carpeta .src del repositorio, es necesario además contar con una cuenta de github y railway.
- **Requisitos de seguridad:** Se requiere contar credenciales de acceso a la cuenta de railway.
- **Diagrama de arquitectura:**
 En el siguiente enlace está disponible el diagrama de [Arquitectura para despliegue](https://app.diagrams.net/#G1yBltl7eknhOu7JDEt-ZWTuk2TM9syxyZ#%7B%22pageId%22:%22tl2pv00i1nYxGFmDqKse%22%7D) 

## Código de despliegue

- **Archivo principal:** El código para despliegue está contenido dentro del archivo main.py en la carpeta src en el repositorio del proyecto.  
- **Rutas de acceso a los archivos:** Para el despliegue puede partirse del script en la ruta: src/main_1.py del repositorio del proyecto.
- **Variables de entorno:**  Para el proyecto no han sido definidas variables de entorno.

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** Se dispone el modelo almacenado en el archivo  best_model.h5-2.keras en espacio en drive y se versiona con dvc, para luego ser cargado desde el código de Fast API.
- **Instrucciones de uso:** Se debe cargar una imagen en formato .png , usando el método post del protocolo HTTP, ejecutar y esperar la respuesta que contendrá la predicción en un formato json.
- **Instrucciones de mantenimiento:** Se complementará en la entrega final.
