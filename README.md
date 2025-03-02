# bigdata_actividad_1_Maria_Arenas

# Proyecto: Trazabilidad y Automatización con GitHub Actions
Descripción breve de la solución
Este proyecto implementa una solución automatizada para la ingesta y almacenamiento de datos desde una API externa. Los datos son procesados y guardados en diferentes formatos (JSON y TXT) y se automatizan pruebas y evidencias mediante GitHub Actions. Esto asegura trazabilidad y reproducibilidad en la ejecución de los scripts.

# Descripción de la automatización mediante GitHub Actions
Se ha configurado un flujo de trabajo automatizado mediante GitHub Actions en el archivo .github/workflows/workflow.yml. Este workflow se activa automáticamente al realizar un push a la rama principal (main) e incluye los siguientes pasos:

Verificación del repositorio: Se clonan los archivos y se validan las rutas.

Instalación de dependencias: Se instalan las librerías definidas en requirements.txt.

Ejecución del script: Se ejecuta el script principal para verificar el correcto funcionamiento.

Generación de evidencias: Verifica que los archivos JSON y TXT hayan sido creados en la carpeta correspondiente.

# La ruta que se creo fue:

Para acceder al sistema de archivos del repositorio y verificarlos en: src/ibgd/static/db/.