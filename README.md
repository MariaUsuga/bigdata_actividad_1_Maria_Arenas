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

# ACTIVIDAD 2

Limpieza de Datos y Auditoría

Este proyecto realiza la ingesta de datos desde una API, específicamente información de amiibos de Nintendo. Durante el proceso, se aplica una limpieza de datos para asegurar la calidad de la información. Esto incluye el reemplazo de valores nulos en la columna "pais" con el valor "Colombia".

Para mantener un registro transparente de las modificaciones, se realiza una auditoría que compara la versión original de los datos (con valores nulos) con la versión modificada (con "Colombia"). Esta auditoría se lleva a cabo mediante la creación de dos archivos CSV: datos_db_original.csv y datos_db_modificado.csv.

Se hace limpieza de datos, se reemplazan los valores null, se llenan por pais Colombia, tambien se eliminan los valores duplicados del dataframe.

El script ingestion.py es el encargado de realizar tanto la ingesta como la limpieza y la auditoría. Este script:

Obtiene los datos de la API y los carga en un DataFrame de pandas.
Guarda la versión original de los datos en datos_db_original.csv.
Reemplaza los valores nulos en la columna "pais" con "Colombia".
Guarda la versión modificada de los datos en datos_db.csv.
Realiza una auditoría comparando ambos archivos CSV y genera un archivo JSON con los resultados.
Este proceso asegura que los datos sean precisos y que se mantenga un registro de las transformaciones realizadas.

NOTA: Los commit se ejecutan de manera correcta en el archivo proyecto_integrador1.yml
Ruta completa: .github/workflows dentro archivo proyecto_integrador1.yml


PASO A PASO realizado en la actividad 2 y explicacion para clonar el repositorio:

Proyecto de Limpieza de Datos y Auditoría
Este repositorio contiene un script de Python (cleaning.py) que realiza la limpieza de datos obtenidos de una API de amiibo de Nintendo, así como un script de ingestión de datos desde una API de criptomonedas (ingestion.py). Se documenta la trazabilidad del proceso y se automatiza la ejecución del script de limpieza mediante GitHub Actions.

Estructura del Proyecto
tu_repositorio/
├── .github/
│   └── workflows/
│       └── main.yml    #proyecto_integrador1.yml
├── src/
│   └── ibgd/
│       └── static/
│           └── cleaning.py
│           └── ingestion.py
├── README.md


Requisitos
Python 3.6 o superior
Bibliotecas de Python: pandas, requests


Instrucciones de Instalación
Clonar el repositorio:

Bash

git clone https://https://github.com/MariaUsuga/bigdata_actividad_1_Maria_Arenas.git
cd tu_repositorio

Ejecución del Script de Limpieza
Para ejecutar el script de limpieza manualmente, ejecuta el siguiente comando:

Bash

python src/ibgd/static/cleaning.py
Esto descargará datos de la API de amiibo, realizará la limpieza (eliminación de duplicados y reemplazo de valores nulos), generará archivos CSV con los datos originales y modificados, un archivo CSV con una muestra representativa, un archivo de auditoría y un archivo JSON con los datos limpios.

Ejecución del Script de Ingestión
Para ejecutar el script de ingestión manualmente, ejecuta el siguiente comando:

Bash

python src/ibgd/static/ingestion.py
Esto descargará datos de la API de criptomonedas, los guardará en archivos JSON y TXT, y generará un archivo de auditoría.

Workflow de GitHub Actions
El workflow de GitHub Actions automatiza la ejecución del script de limpieza cada vez que se realiza un push a la rama main.

Descripción del Workflow
El archivo main.yml en .github/workflows/ define el workflow. Este workflow realiza los siguientes pasos:

Checkout del repositorio: Clona el repositorio en el entorno de GitHub Actions.
Configuración de Python: Configura el entorno de Python con la versión especificada.
Instalación de dependencias: Instala las bibliotecas pandas y requests.
Ejecución del script de limpieza: Ejecuta el script cleaning.py.
Commit y push de cambios: Hace commit y push de los archivos generados (CSV, auditoría, JSON) a la rama main.
Configuración del Workflow
El workflow se activa automáticamente en cada push a la rama main. No se requiere configuración adicional.

Trazabilidad del Proceso
El script cleaning.py genera los siguientes archivos para documentar la trazabilidad del proceso:

datos_db_original.csv: Contiene los datos originales descargados de la API.
datos_db_modificado.csv: Contiene algunos de los datos modificados en la limpieza de datos de la API.
datos_db.csv: Contiene los datos después de la limpieza, la utlima columna de pais se llena completa con el nombre colombia.
cleaning_report.txt: Contiene un informe de auditoría con el número de registros antes y después de la limpieza, y las operaciones realizadas.
ingestion.json: Contiene los datos limpios en formato JSON.
El script ingestion.py genera los siguientes archivos para documentar la trazabilidad del proceso:

ingestion.json: Contiene los datos de la API de criptomonedas en formato JSON.
ingestion.txt: Contiene los datos de la API de criptomonedas en formato TXT.
ingestion_audit.txt: Contiene un informe de auditoría con los datos de entrada, los datos guardados y la cantidad de registros y columnas.


# ENTREGA ACTIVIDAD 3

Se crea el archivo transformation.py, donde se crea los Dataframe, se hace un Join para unir los dos dataframe, con lo pide la actividad.

Tambien se crea un archivo de auditoria transformation.txt y 
Dataset enriquecido.csv

