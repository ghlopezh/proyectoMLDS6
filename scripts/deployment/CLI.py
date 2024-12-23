
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from IPython.display import display
os.system('pip install mlflow')
import mlflow
import mlflow.keras
from IPython import get_ipython

from argparse import ArgumentParser

command = """
mlflow server \
        --backend-store-uri sqlite:///tracking.db \
        --default-artifact-root file:mlruns \
        -p 5000 &
"""
#get_ipython().system_raw(command)

import subprocess

#command = "tu_comando"  # Reemplaza con el comando que quieres ejecutar
subprocess.run(command, shell=True) 

# Definir parámetros
model_path = "/content/best_model.h5-2.keras"  # Ruta del modelo
image_path = "/content/00000578_000.png"  # Ruta de la imagen a predecir
img_height = 224
img_width = 224

mlflow.set_tracking_uri("http://localhost:5000")
# Inicializar MLflow
#mlflow.set_tracking_uri("file:///content/mlruns")  # Guardar localmente en Colab
experiment_name = "resnet50_experiment"

# Crear o cargar el experimento
try:
    exp_id = mlflow.create_experiment(experiment_name)
except:
    exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

# Cargar el modelo preentrenado
model = load_model(model_path)

# Procesar la imagen para predicción
def preprocess_image1(img_path, target_size):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalización
    return img_array

# Preparar la imagen
input_image = preprocess_image1(image_path, target_size=(img_height, img_width))

# Realizar predicción
with mlflow.start_run(run_name="resnet50_model", experiment_id=exp_id):
   # predictions = model.predict(input_image)
   # predicted_class = np.argmax(predictions[0])  # Obtener la clase con mayor probabilidad
   # confidence = np.max(predictions[0])  # Confianza de la predicción

    # Registrar modelo en MLflow
    # mlflow.keras.log_model(model, "resnet50_model")
    mlflow.keras.log_model(model, "resnet50_model", registered_model_name="jobclf")


# Configurar la URI de seguimiento de MLflow
#mlflow.set_tracking_uri("http://localhost:5000")

# Preprocesar la imagen para que coincida con el modelo
def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)  # Cargar imagen
    img_array = image.img_to_array(img)                      # Convertir a array
    img_array = np.expand_dims(img_array, axis=0)            # Expandir dimensiones
    img_array /= 255.0                                       # Normalización [0, 1]
    return img_array

# Función principal
def main():
    # Configurar argumentos
    parser = ArgumentParser(
        description="CLI para clasificación de imágenes usando modelo en MLflow"
    )
    parser.add_argument(
        "--image_path",
        type=str,
        required=True,
        help="Ruta a la imagen en formato PNG"
    )
    args = parser.parse_args()  # Parsear argumentos

    # Cargar el modelo desde MLflow Model Registry
    model = mlflow.pyfunc.load_model("models:/jobclf/1")

    # Preprocesar la imagen
    input_image = preprocess_image(args.image_path)

    # Realizar predicción
    prediction = model.predict(input_image)
    predicted_class = np.argmax(prediction[0])  # Clase predicha
    confidence = np.max(prediction[0])          # Confianza

    # Mostrar resultados
    print(f"Clase predicha: {predicted_class}")
    print(f"Confianza: {confidence:.2f}")

if __name__ == "__main__":
    main()
