import os
os.system('pip install fastapi python-multipart')
from fastapi import FastAPI, HTTPException, File, UploadFile
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Inicializar la app de FastAPI
app = FastAPI()

# Cargar el modelo previamente entrenado (ResNet50 en formato .h5)
model = load_model("/content/sample_data/best_model.h5-2.keras")

# Función para preprocesar la imagen
def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Preprocesa la imagen para que sea compatible con ResNet50.
    Convierte a RGB, redimensiona a 224x224 y normaliza los valores.
    """
    image = image.convert("RGB")  # Asegurarse de que tenga 3 canales (RGB)
    image = image.resize((224, 224))  # ResNet50 espera 224x224
    image_array = np.array(image) / 255.0  # Normalizar a rango [0, 1]

    # Normalización de ResNet50 (opcional, según cómo entrenaste el modelo)
    mean = np.array([0.485, 0.456, 0.406])  # Promedios de ResNet
    std = np.array([0.229, 0.224, 0.225])  # Desviaciones estándar de ResNet
    image_array = (image_array - mean) / std
    image_array = np.expand_dims(image_array, axis=0)  # Agregar dimensión para lotes
    return image_array

# Endpoint para realizar predicciones
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint para predecir si en una imagen de rayos X se detecta enfermedad.
    """
    try:
        # Validar el tipo de archivo
        if file.content_type != "image/png":
            raise HTTPException(status_code=400, detail="Solo se aceptan imágenes PNG.")

        # Cargar y procesar la imagen
        image = Image.open(file.file)
        processed_image = preprocess_image(image)

        # Realizar la predicción
        prediction = model.predict(processed_image)
        result = prediction.tolist()  # Convertir la predicción a un formato serializable

        return {
            "filename": file.filename,
            "prediction": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando la imagen: {str(e)}")
