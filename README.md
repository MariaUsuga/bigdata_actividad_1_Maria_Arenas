# bigdata_actividad_1_Maria_Arenas

# Proyecto: Trazabilidad y Automatización con GitHub Actions
Descripción breve de la solución
Este proyecto implementa una solución automatizada para la ingesta y almacenamiento de datos desde una API externa. Los datos son procesados y guardados en diferentes formatos (JSON y TXT) y se automatizan pruebas y evidencias mediante GitHub Actions. Esto asegura trazabilidad y reproducibilidad en la ejecución de los scripts.

# Descripción de la automatización mediante GitHub Actions
Se ha configurado un flujo de trabajo automatizado mediante GitHub Actions en el archivo .github/workflows/workflow.yml. Este workflow se activa automáticamente al realizar un push a la rama principal (main) e incluye los siguientes pasos:

Verificación del repositorio: Se clonan los archivos y se validan las rutas.

Ejecución del script: Se ejecuta el script principal para verificar el correcto funcionamiento.

Generación de evidencias: Verifica que los archivos JSON y TXT hayan sido creados en la carpeta correspondiente.

# La ruta que se creo fue:

Para acceder al sistema de archivos del repositorio y verificarlos: src/ibgd/static/ingestion.py

auditoria: contiene el archivo ingestion_audit.txt que hace su respectivo control e informe de numero de registros y columnas, en la carpeta db esta la base de datos.

ACTIVIDAD 2

Limpieza de Datos y Auditoría

Este proyecto realiza la ingesta de datos desde una API, específicamente información de amiibos de Nintendo. Durante el proceso, se aplica una limpieza de datos para asegurar la calidad de la información. Esto incluye el reemplazo de valores nulos en la columna "pais" con el valor "Colombia".

Para mantener un registro transparente de las modificaciones, se realiza una auditoría que compara la versión original de los datos (con valores nulos) con la versión modificada (con "Colombia"). Esta auditoría se lleva a cabo mediante la creación de dos archivos CSV: datos_db_original.csv y datos_db_modificado.csv.

El script ingestion.py es el encargado de realizar tanto la ingesta como la limpieza y la auditoría. Este script:

Obtiene los datos de la API y los carga en un DataFrame de pandas.
Guarda la versión original de los datos en datos_db_original.csv.
Reemplaza los valores nulos en la columna "pais" con "Colombia".
Guarda la versión modificada de los datos en datos_db_modificado.csv.
Realiza una auditoría comparando ambos archivos CSV y genera un archivo JSON con los resultados.
Este proceso asegura que los datos sean precisos y que se mantenga un registro de las transformaciones realizadas.
