import pandas as pd
import os

class Transformation:
    def __init__(self):
        self.ruta_static = "src/ibgd/static/"

    def dataset_1(self):
        try:
            # Cargar datos desde un archivo CSV de la API procesada
            df_1 = pd.read_csv(f"{self.ruta_static}datos_dataset1.csv")
            print("Se generó df_1 a partir de datos_dataset1.csv.")
            return df_1
        except FileNotFoundError:
            print("El archivo 'datos_dataset1.csv' no se encuentra en la ruta especificada.")
            return pd.DataFrame()

    def dataset_2(self):
        try:
            # Cargar datos desde un archivo CSV local
            df_2 = pd.read_csv(f"{self.ruta_static}datos_local.csv")
            print("Se generó df_2 a partir de datos_local.csv.")
            return df_2
        except FileNotFoundError:
            print("El archivo 'datos_local.csv' no se encuentra en la ruta especificada.")
            return pd.DataFrame()

    def join_dataset(self, df_1=pd.DataFrame(), df_2=pd.DataFrame(), nom_col1="", nom_col2=""):
        if df_1.empty or df_2.empty:
            print("Uno de los DataFrames está vacío. No se puede realizar el cruce.")
            return pd.DataFrame()
        try:
            # Realizar el cruce (merge) entre df_1 y df_2
            df_3 = pd.merge(df_1, df_2, left_on=nom_col1, right_on=nom_col2, how="inner")
            print("Se generó df_3 mediante la unión de dataset_1 y dataset_2.")
            return df_3
        except KeyError as e:
            print(f"Error en el cruce: {e}. Verifica los nombres de las columnas para la unión.")
            return pd.DataFrame()

    def auditoria(self, df=pd.DataFrame()):
        if df.empty:
            print("El DataFrame está vacío. No se puede generar auditoría.")
            return False
        try:
            # Generar archivo de auditoría
            ruta_auditoria = f"{self.ruta_static}auditoria_transformation.txt"
            with open(ruta_auditoria, "w") as auditoria_file:
                auditoria_file.write("Informe de Auditoría de Transformación\n\n")
                auditoria_file.write(f"Número de registros: {len(df)}\n")
                auditoria_file.write(f"Número de columnas: {len(df.columns)}\n")
                auditoria_file.write("\nOperaciones realizadas:\n")
                auditoria_file.write("- Se unieron dataset_1 y dataset_2.\n")
                auditoria_file.write("- Se generó un DataFrame resultante (df_3).\n")
            print("Archivo de auditoría generado correctamente en 'auditoria_transformation.txt'.")
            return True
        except Exception as error:
            print(f"Error al generar la auditoría: {error}")
            return False

    def ejecucion(self):
        # Cargar datasets
        df1 = self.dataset_1()
        df2 = self.dataset_2()

        # Realizar cruce y obtener dataset enriquecido
        df_enriquecido = self.join_dataset(df1, df2, nom_col1="id_columna1", nom_col2="id_columna2")

        if not df_enriquecido.empty:
            # Generar muestra representativa
            muestra = df_enriquecido.sample(frac=0.1)  # Muestra del 10%
            ruta_muestra = f"{self.ruta_static}muestra_dataset_enriquecido.csv"
            muestra.to_csv(ruta_muestra, index=False)
            print(f"Muestra representativa guardada en '{ruta_muestra}'.")

            # Generar auditoría
            if self.auditoria(df_enriquecido):
                print("Proceso completado y dataset enriquecido generado correctamente.")
        else:
            print("No se generó un DataFrame enriquecido. Revisa los pasos anteriores.")

# Ejecutar la clase Transformation
trx = Transformation()
trx.ejecucion()