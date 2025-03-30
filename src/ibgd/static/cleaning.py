import pandas as pd
import requests
import json

class Cleaning:
    def __init__(self):
        self.ruta_static = "src/ibgd/static/"

    def obtener_datos(self):
        # Simula la obtención de datos de una API
        try:
            url = "https://www.amiiboapi.com/api/amiibo/?name=mario"
            response = requests.get(url)
            response.raise_for_status()
            datos = response.json().get("amiibo", [])
            if datos:
                return pd.DataFrame(datos)
            else:
                print("No se obtuvieron datos.")
                return pd.DataFrame()
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return pd.DataFrame()

    def limpiar_datos(self, df):
        if df.empty:
            print("El DataFrame está vacío. No se pueden limpiar datos.")
            return df

        try:
            # Guardar los datos originales
            df.to_csv(f"{self.ruta_static}datos_db_original.csv", index=False)

            # Eliminar duplicados
            df = df.drop_duplicates()

            # Manejar valores nulos
            if "pais" not in df.columns:
                df["pais"] = None
            df["pais"] = df["pais"].fillna("Colombia")

            # Guardar datos limpios
            df.to_csv(f"{self.ruta_static}datos_db_modificado.csv", index=False)
            print("Datos limpiados y guardados correctamente.")
            return df
        except Exception as e:
            print(f"Error al limpiar datos: {e}")
            return pd.DataFrame()

    def generar_auditoria(self, df):
        try:
            ruta_auditoria = f"{self.ruta_static}cleaning_report.txt"
            with open(ruta_auditoria, "w") as archivo_auditoria:
                archivo_auditoria.write("Informe de Auditoría de Limpieza\n\n")
                archivo_auditoria.write(f"Número de registros iniciales: {len(df)}\n")
                archivo_auditoria.write("Operaciones realizadas:\n- Eliminación de duplicados\n- Manejo de valores nulos en la columna 'pais'\n")
            print(f"Archivo de auditoría generado: {ruta_auditoria}")
        except Exception as e:
            print(f"Error al generar auditoría: {e}")

    def ejecutar(self):
        # Obtener y limpiar datos
        df = self.obtener_datos()
        if not df.empty:
            df_limpio = self.limpiar_datos(df)
            self.generar_auditoria(df_limpio)
        else:
            print("No se realizó ninguna limpieza debido a la falta de datos.")

# Ejecución del script
cleaning = Cleaning()
cleaning.ejecutar()