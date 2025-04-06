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

Tambien se crea un archivo de auditoria transformation.txt y Dataset enriquecido.csv

A continuacion se hace la Descripcion y trazabilidad de la entrega 3 y como clonar el proyecto.

# Proyecto de Enriquecimiento de Datos

Este repositorio contiene un flujo de trabajo para la ingesta, limpieza, transformación y enriquecimiento de datos, diseñado para automatizar procesos mediante GitHub Actions.


# Estructura del Proyecto

Ingesta (ingestion.py): Obtención de datos desde una API, almacenamiento en formatos JSON y TXT, y generación de auditorías.

Limpieza (cleaning.py): Eliminación de duplicados, manejo de valores nulos, y exportación de datos limpios.

Transformación (Transformation.py): Unión de datasets (API y local), integración de datos y generación de un dataset enriquecido.

Automatización: Implementación de un workflow automatizado utilizando GitHub Actions.


# Pasos para Clonar el Repositorio:

1. Clona el repositorio en tu máquina local:
git clone https://github.com/MariaUsuga/bigdata_actividad_1_Maria_Arenas.git
cd tu_repositorio
2. Crea un entorno virtual e instálalo:
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
3. Instala las dependencias del proyecto:
pip install -r requirements.txt


# Automatización mediante GitHub Actions

El flujo de trabajo está configurado en el archivo proyecto_integrador1.yml ubicado en github/workflows/. A continuación se detalla su funcionamiento:
Eventos que activan el workflow:
Cada vez que se realiza un push a la rama main.
Tareas ejecutadas:
Configuración del entorno de ejecución (Python 3.9).
Instalación de dependencias.
Ejecución de los scripts de ingesta, limpieza y transformación.
Commit y push automático de los resultados generados.

# Archivos Generados

Dataset enriquecido: Archivo CSV con datos finales (muestra_dataset_enriquecido.csv).
Auditorías: Informes en formato txt. que documentan cada paso del proceso.
Datos limpios: Archivos CSV intermedios, como datos_db_modificado.csv

# ENTREGA ACTIVIDAD 4

Descripción General: La Entrega 4 del proyecto se enfoca en la fase de enriquecimiento de datos, donde se integran los datos obtenidos de las API de amiibo de Nintendo y criptomonedas, mejorando la calidad de la información y optimizando su valor para los análisis posteriores. Esta fase se lleva a cabo mediante la creación de un script de transformación que une los conjuntos de datos en un dataset enriquecido. Adicionalmente, se implementa una automatización avanzada mediante GitHub Actions para ejecutar la ingesta, limpieza, transformación y enriquecimiento de los datos de manera continua y eficiente.

Objetivos de la Entrega:Transformación y Enriquecimiento de Datos: Se integran los datos obtenidos de las APIs en un único conjunto, aplicando transformaciones y enriquecimientos adicionales, con el fin de hacer los datos más completos y útiles.

Automatización del Proceso: Se automatizan todas las etapas del flujo de trabajo (ingesta, limpieza, transformación y enriquecimiento) a través de GitHub Actions, asegurando que los procesos se ejecuten de manera continua con cada nueva actualización del repositorio.

Documentación de la Trazabilidad: Se documenta todo el proceso de transformación y enriquecimiento mediante un archivo de auditoría, que asegura la trazabilidad de los cambios realizados a los datos.

Flujo de Trabajo
El flujo de trabajo implementado en esta entrega incluye los siguientes pasos clave:

Ingesta de Datos: Obtención de los datos desde las APIs de amiibo de Nintendo y criptomonedas mediante los scripts ingestion.py y cleaning.py.

Limpieza de Datos: Se realiza una limpieza de los datos, que incluye la eliminación de duplicados y el reemplazo de valores nulos, como se detalló en las entregas anteriores.

Transformación y Enriquecimiento:

Se crea el script transformation.py, que une los datasets de las APIs y los datos locales en un solo dataset enriquecido.

Se generan los archivos de auditoría correspondientes, como transformation.txt y Dataset_enriquecido.csv.

Automatización con GitHub Actions:

Se configura un workflow en el archivo .github/workflows/proyecto_integrador1.yml, que automatiza la ejecución del proceso completo cada vez que se realice un push a la rama principal (main).

El workflow incluye la ejecución de los scripts de ingesta, limpieza, transformación y la subida de los resultados generados a la rama principal.

Componentes Principales
Script de Ingesta (ingestion.py): Obtiene los datos desde las APIs de amiibo de Nintendo y criptomonedas, y los guarda en archivos JSON y TXT.

Script de Limpieza (cleaning.py): Realiza la limpieza de los datos, eliminando duplicados y gestionando valores nulos.

Script de Transformación (transformation.py): Realiza la unión de los datasets de amiibo y criptomonedas, generando un dataset enriquecido y un archivo de auditoría.

Automatización con GitHub Actions: Se configura un flujo de trabajo automatizado para ejecutar todos los scripts de procesamiento y almacenar los resultados en el repositorio.

Archivos Generados
Durante la ejecución del proceso, se generan los siguientes archivos:

Archivos de Datos:

datos_db_original.csv: Contiene los datos originales descargados de las APIs.

datos_db_modificado.csv: Contiene los datos después de la limpieza.

datos_db.csv: Contiene los datos después de la limpieza, con los valores nulos reemplazados por "Colombia" en la columna pais.

muestra_dataset_enriquecido.csv: Contiene el dataset final enriquecido con los datos combinados de las APIs y las transformaciones realizadas.

Archivos de Auditoría:

cleaning_report.txt: Reporte de auditoría generado durante la limpieza de datos, indicando el número de registros antes y después de la limpieza.

ingestion_audit.txt: Reporte de auditoría generado durante la ingesta de datos, con información sobre el número de registros obtenidos y almacenados.

transformation.txt: Reporte de auditoría generado durante la transformación, con información sobre el proceso de unión de los datasets y los registros involucrados.

Otros Archivos Generados:

ingestion.json: Contiene los datos obtenidos de la API de criptomonedas en formato JSON.

ingestion.txt: Contiene los datos de la API de criptomonedas en formato TXT.