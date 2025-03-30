import requests
import pandas as pd
import json
import os

class Ingestion:
    def __init__(self):
        self.ruta_static = "src/ibgd/static/"

    def obtener_db(self, url="", params={}):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return pd.DataFrame(response.json()["amiibo"])
        except requests.exceptions.RequestException as error:
            print(error)
            return pd.DataFrame()

    def cargar_a_csv(self, df):
        try:
            # Guardar la versión original en un archivo CSV
            ruta_original = "datos_db_original.csv"
            df.to_csv(ruta_original, index=False)

            # Eliminar duplicados del DataFrame
            df_sin_duplicados = df.drop_duplicates()

            # Reemplazar valores nulos en la columna "pais" con "Colombia"
            df_sin_duplicados["pais"] = df_sin_duplicados["pais"].fillna("Colombia")

            # Guardar la versión modificada en un archivo CSV
            ruta_modificada = "datos_db_modificado.csv"
            df_sin_duplicados.to_csv(ruta_modificada, index=False)

            # Guardar una muestra representativa en un archivo CSV
            muestra_representativa = df_sin_duplicados.sample(n=min(10, len(df_sin_duplicados)))  # Muestra de 10 registros o menos
            ruta_muestra = "muestra_registros_limpios.csv"
            muestra_representativa.to_csv(ruta_muestra, index=False)

            # Generar el archivo de auditoría
            ruta_auditoria = "cleaning_report.txt"
            with open(ruta_auditoria, "w") as archivo_auditoria:
                archivo_auditoria.write("Informe de Auditoría de Limpieza de Datos\n\n")
                archivo_auditoria.write(f"Número de registros antes de la limpieza: {len(df)}\n")
                archivo_auditoria.write(f"Número de registros después de la limpieza: {len(df_sin_duplicados)}\n\n")
                archivo_auditoria.write("Operaciones realizadas:\n")
                archivo_auditoria.write("- Eliminación de duplicados\n")
                archivo_auditoria.write("- Reemplazo de valores nulos en la columna 'pais' con 'Colombia'\n")

            # Guardar los datos en un archivo JSON para la auditoría
            datos_json = df_sin_duplicados.to_dict(orient="records")
            ruta_json = "{}db/ingestion.json".format(self.ruta_static)
            with open(ruta_json, "w") as archivo_json:
                json.dump(datos_json, archivo_json)

            print("Datos cargados correctamente en CSV (original y modificado), muestra representativa y archivo de auditoría.")
        except Exception as error:
            print("Error al cargar datos:", error)

    def validar_autoria(self, datos, nombre_archivo="ingestion"):
        """
        Valida la cantidad de registros y columnas de la variable 'datos'
        y de los archivos CSV (original y modificado).
        Se asume que 'datos' es un DataFrame.
        """
        try:
            # Leer los datos del archivo CSV original
            df_archivo_original = pd.read_csv("datos_db_original.csv")

            # Leer los datos del archivo CSV modificado
            df_archivo_modificado = pd.read_csv("datos_db_modificado.csv")

            # Validación de la variable 'datos'
            registros_datos = len(datos)
            columnas_datos = len(datos.columns)

            # Validación del archivo CSV original
            registros_archivo_original = len(df_archivo_original)
            columnas_archivo_original = len(df_archivo_original.columns)

            # Validación del archivo CSV modificado
            registros_archivo_modificado = len(df_archivo_modificado)
            columnas_archivo_modificado = len(df_archivo_modificado.columns)

            print("Variable 'datos': {} registros, {} columnas".format(registros_datos, columnas_datos))
            print("Archivo CSV Original: {} registros, {} columnas".format(registros_archivo_original, columnas_archivo_original))
            print("Archivo CSV Modificado: {} registros, {} columnas".format(registros_archivo_modificado, columnas_archivo_modificado))

            # Comparar la cantidad de registros y columnas en ambas versiones
            registros_iguales = (registros_archivo_original == registros_archivo_modificado)
            columnas_iguales = (columnas_archivo_original == columnas_archivo_modificado)

            return (registros_datos == registros_archivo_modificado) and (columnas_datos == columnas_archivo_modificado) and registros_iguales and columnas_iguales
        except Exception as e:
            print("Error al validar la auditoría:", e)
            return False

# Uso de la clase Ingestion
ingestion = Ingestion()
url = "https://www.amiiboapi.com/api/amiibo/?name=mario"
df_datos = ingestion.obtener_db(url=url)

if not df_datos.empty:
    if "pais" not in df_datos.columns:
        df_datos["pais"] = None  # Crea la columna si no existe
    df_datos["pais"] = df_datos["pais"].fillna("NULL")  # Asegurar que los valores nulos sean NULL antes de cargar
    ingestion.cargar_a_csv(df_datos)
    ingestion.validar_autoria(datos=df_datos)  # Pasar el DataFrame a la auditoría
else:
    print("No se obtuvieron datos de la API.")


# Eliminar duplicados y manejar valores nulos
df_api = df_api.drop_duplicates()
if "pais" not in df_api.columns:
    df_api["pais"] = None
df_api["pais"] = df_api["pais"].fillna("Colombia")

# Guardar datos limpios
df_api.to_csv("datos_api_limpio.csv", index=False)
print("Datos limpios guardados en 'datos_api_limpio.csv'.")    