import requests
import json
from datetime import datetime

class Ingestion:
    def __init__(self):
        self.ruta_static = "src/ibgd/static/"

    def obtener_datos_api(self, url="", params={}):
        url = "{}/{}/{}/".format(url, params["coin"], params["method"])
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(error)
            return {}

    def guardar_datos_json(self, datos={}, nombre_archivo="ingestion"):
        with open("{}db/{}.json".format(self.ruta_static, nombre_archivo), "w") as archivo:
            json.dump(datos, archivo)

    def guardar_datos_txt(self, datos={}, nombre_archivo="ingestion"):
        archivo_txt = "{}db/{}.txt".format(self.ruta_static, nombre_archivo)
        archivo_auditoria = "{}auditoria/{}_audit.txt".format(self.ruta_static, nombre_archivo)
        
        # Guardar datos en archivo txt
        with open(archivo_txt, "w") as archivo:
            for clave, valor in datos.items():
                archivo.write(f"{clave}: {valor}\n")
        
        # Guardar auditoría
        with open(archivo_auditoria, "a") as audit_file:
            audit_file.write(f"Fecha y hora: {datetime.now()}\n")
            audit_file.write("Datos de entrada:\n")
            audit_file.write(json.dumps(datos, indent=4))
            audit_file.write("\nDatos guardados en archivo txt:\n")
            with open(archivo_txt, "r") as archivo:
                audit_file.write(archivo.read())
            # Agregar cantidad de registros y columnas
            num_registros = len(datos)
            num_columnas = len(next(iter(datos.values()))) if datos else 0
            audit_file.write(f"\nCantidad de registros: {num_registros}\n")
            audit_file.write(f"Cantidad de columnas: {num_columnas}\n")
            audit_file.write("\n\n")

    def validar_auditoria_txt(self, datos={}, nombre_archivo="ingestion"):
        archivo_auditoria = "{}auditoria/{}_audit.txt".format(self.ruta_static, nombre_archivo)
        try:
            with open(archivo_auditoria, "r") as audit_file:
                contenido = audit_file.read()
                print("Contenido del archivo de auditoría:")
                print(contenido)
        except FileNotFoundError:
            print("El archivo de auditoría no existe.")

    def guardar_db(self, datos={}, nombre_archivo="ingestion"):
        pass            

# Uso de la clase Ingestion
ingestion = Ingestion()
parametros = {"coin": "BTC", "method": "ticker"}
url = "https://www.mercadobitcoin.net/api"


# Obtener datos y convertir a DataFrame
datos_api = ingestion.obtener_datos_api(url=url, params=parametros)
df_api = pd.DataFrame(datos_api)


datos = ingestion.obtener_datos_api(url=url, params=parametros)

if len(datos) > 0:
    print(json.dumps(datos, indent=4))
else:
    print("No se obtuvieron datos")

ingestion.guardar_datos_json(datos=datos, nombre_archivo="ingestion")
ingestion.guardar_datos_txt(datos=datos, nombre_archivo="ingestion")

ingestion.validar_auditoria_txt(datos=datos, nombre_archivo="ingestion")