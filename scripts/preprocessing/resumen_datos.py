
#Definir las rutas de los archivos
csv_path = '/content/proyectoMLDS6/docs/data/data_Data_Entry_2017_v2020_ESTADO_SALUD.csv'
df = pd.read_csv(csv_path, sep=';')

# Separar el conjunto de datos entre entrenamiento y prueba
train_df = df[df['Image Index'].isin([os.path.basename(path) for path in train_files])]
test_df = df[df['Image Index'].isin([os.path.basename(path) for path in test_files])]


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


## Peso total de los archivos
peso = !du -sh /root/.cache/huggingface/datasets/downloads/extracted/ac866273977ae75ab1ad5e5f4cbef6f220bf1511db65b340d8a024565b33b856/images
peso

##  Numero de archivos
#cantidad = !ls -1 /root/.cache/huggingface/datasets/downloads/extracted/ac866273977ae75ab1ad5e5f4cbef6f220bf1511db65b340d8a024565b33b856/images | wc -l
#cantidad

# Resumen de los datos 
#import imghdr
#imghdr.what('/content/images/00028523_019.png')

def count_file_formats(folder_path):
  """
  Identifica todos los tipos de formato de los archivos en la carpeta especificada
  y retorna el número de documentos por cada tipo de formato.

  Args:
    folder_path: La ruta a la carpeta que se desea analizar.

  Returns:
    Un diccionario donde las claves son los tipos de formato de archivo
    y los valores son el número de documentos de ese tipo.
  """
  format_counts = {}
  for filename in os.listdir(folder_path):
    # Obtiene la extensión del archivo
    _, extension = os.path.splitext(filename)
    # Si la extensión no está en el diccionario, la agrega con un conteo de 1
    # De lo contrario, incrementa el conteo existente en 1
    format_counts[extension] = format_counts.get(extension, 0) + 1
  return format_counts

image_folder_path = '/root/.cache/huggingface/datasets/downloads/extracted/ac866273977ae75ab1ad5e5f4cbef6f220bf1511db65b340d8a024565b33b856/images'
file_counts = count_file_formats(image_folder_path)
print(file_counts)


## Tipos de variables adicionales 
df = pd.read_csv('/content/data_Data_Entry_2017_v2020_ESTADO_SALUD.csv', sep=';')
df.describe()

