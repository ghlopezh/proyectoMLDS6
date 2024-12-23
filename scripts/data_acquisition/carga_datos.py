
import cv2
import datasets
from datasets import DownloadManager
import os
import pandas as pd
from pandas import read_csv
from requests import get
import torch
import torchvision
import torchvision.transforms as transforms # Importa el modulo transforms


logger = datasets.logging.get_logger(__name__)

_HOMEPAGE = "https://nihcc.app.box.com/v/chestxray-nihcc"
_REPO = "https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset/resolve/main/data"
_IMAGE_URLS = [
	f"{_REPO}/images/images_001.zip",
	#f"{_REPO}/images/images_002.zip",
	#f"{_REPO}/images/images_003.zip",
	#f"{_REPO}/images/images_004.zip",
	#f"{_REPO}/images/images_005.zip",
	#f"{_REPO}/images/images_006.zip",
	#f"{_REPO}/images/images_007.zip",
	#f"{_REPO}/images/images_008.zip",
	#f"{_REPO}/images/images_009.zip",
	#f"{_REPO}/images/images_010.zip",
	#f"{_REPO}/images/images_011.zip",
	#f"{_REPO}/images/images_012.zip"
	#'https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset/resolve/main/dummy/0.0.0/images_001.tar.gz',
	#'https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset/resolve/main/dummy/0.0.0/images_002.tar.gz'
]

_URLS = {
	"train_val_list": f"{_REPO}/train_val_list.txt",
	"test_list": f"{_REPO}/test_list.txt",
	"labels": f"{_REPO}/Data_Entry_2017_v2020.csv",
	"BBox": f"{_REPO}/BBox_List_2017.csv",
	"image_urls": _IMAGE_URLS
}

_LABEL2IDX = {"No Finding": 0,
	     "Atelectasis": 1,
	     "Cardiomegaly": 2,
	     "Effusion": 3,
	     "Infiltration": 4,
	     "Mass": 5,
	     "Nodule": 6,
	     "Pneumonia": 7,
	     "Pneumothorax": 8,
  	     "Consolidation": 9,
	     "Edema": 10,
	     "Emphysema": 11,
	     "Fibrosis": 12,
	     "Pleural_Thickening": 13,
	     "Hernia": 14}

_NAMES = list(_LABEL2IDX.keys())


logger.info("Downloading the train_val_list image names")
train_val_list = get(_URLS['train_val_list']).iter_lines()
train_val_list = set([x.decode('UTF8') for x in train_val_list])
logger.info(f"Check train_val_list: {train_val_list}")

# Create list for store the name of the images for each dataset
train_files = []
test_files = []

dl_manager = DownloadManager()

# Download batches
data_files = dl_manager.download_and_extract(_URLS["image_urls"])


# Iterate trought image folder and check if they belong to the trainset or testset
for batch in data_files:
		logger.info(f"Batch for data_files: {batch}")
		path_files = dl_manager.iter_files(batch)
		for img in path_files:
		    if os.path.basename(img) in train_val_list:
		      train_files.append(img)
		    else:
		      test_files.append(img)

datasets.SplitGenerator(
			name=datasets.Split.TRAIN,
			gen_kwargs={
				"files": train_files
			}
		    ),
datasets.SplitGenerator(
			name=datasets.Split.TEST,
			gen_kwargs={
				"files": test_files
			}
		    )

#Definir las rutas de los archivos
csv_path = '/content/proyectoMLDS6/docs/data/data_Data_Entry_2017_v2020_ESTADO_SALUD.csv'
df = pd.read_csv(csv_path, sep=';')

# Separar el conjunto de datos entre entrenamiento y prueba
train_df = df[df['Image Index'].isin([os.path.basename(path) for path in train_files])]
test_df = df[df['Image Index'].isin([os.path.basename(path) for path in test_files])]


from torch.utils.data import Dataset, DataLoader
#Se crea un dataset personalizado
class ImageDataset(Dataset):
    def __init__(self, file_paths, labels_df, transform=None):
        self.file_paths = file_paths
        self.labels_df = labels_df.set_index('Image Index')  # Usamos el nombre de la imagen como índice
        self.transform = transform

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        img_path = self.file_paths[idx]
        img_name = os.path.basename(img_path)
        label = self.labels_df.loc[img_name, 'ESTADO_SALUD']  # Obtén la etiqueta desde el CSV
        label = int(label) # Convert label to integer
        image = Image.open(img_path).convert("RGB")  # Convertir a RGB para evitar problemas con RGBA

        if self.transform:
            image = self.transform(image)

        return image, label


  #Se definen las transformaciones de datos.
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Redimensiona las imágenes
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # Normalización estándar de ResNet
])

# Crear conjuntos de datos y cargadores de datos
train_dataset = ImageDataset(train_files, train_df, transform=transform)
test_dataset = ImageDataset(test_files, test_df, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)