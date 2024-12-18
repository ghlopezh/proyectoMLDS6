from fastapi import FastAPI, HTTPException, File, UploadFile
from PIL import Image
import numpy as np
import joblib

# Inicializar la app de FastAPI
app = FastAPI()

# Cargar el modelo previamente entrenado (ResNet)
model = joblib.load("resnet_model.joblib")

# Función para preprocesar la imagen
def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Preprocesa la imagen para que sea compatible con ResNet.
    Convierte a RGB, redimensiona a 224x224 y normaliza los valores.
    """
    image = image.convert("RGB")  # Asegurarse de que tenga 3 canales (RGB)
    image = image.resize((224, 224))  # ResNet espera 224x224
    image_array = np.array(image) / 255.0  # Normalizar a rango [0, 1]
    # Normalización de ResNet (opcional, según cómo entrenaste el modelo)
    mean = np.array([0.485, 0.456, 0.406])  # Promedios de ResNet
    std = np.array([0.229, 0.224, 0.225])  # Desviaciones estándar de ResNet
    image_array = (image_array - mean) / std
    image_array = np.transpose(image_array, (2, 0, 1))  # Cambiar a formato CHW
    return np.expand_dims(image_array, axis=0)  # Agregar dimensión para lotes

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
        result = int(prediction[0])  # Convertir a entero (0 o 1)

        return {
            "filename": file.filename,
            "prediction": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando la imagen: {str(e)}")
