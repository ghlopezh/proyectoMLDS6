
from argparse import ArgumentParser
#import mlflow
#mlflow.set_tracking_uri("http://localhost:5000")

def main():
    parser = ArgumentParser(
            description="CLI para identificación de enfermedad a partir de radiografía de tórax"
            )
    parser.add_argument("--text", type=str, required=True, help="Texto con la descripción del trabajo")
    args = parser.parse_args()
    #model = mlflow.pyfunc.load_model("models:/jobclf/1")
    model = joblib.load("resnet_model.joblib") 
    prediction = model.predict([args.text])[0]
    prediction = "enfermo" if prediction else "sano"
    print(f"El paciente esta: {prediction}")

if __name__ == "__main__":
    main()
