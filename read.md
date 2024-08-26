# Image Similarity Checker

Este proyecto es una aplicación web que permite verificar si una imagen subida es similar a las imágenes almacenadas en una carpeta específica en el servidor. Utiliza Flask y OpenCV para realizar la comparación de imágenes.

## Características

- Permite subir una imagen y verificar su similitud con imágenes existentes.
- Muestra todas las imágenes similares encontradas en la interfaz web.

## Tecnologías Utilizadas

- **Flask**: Framework web para desarrollar la aplicación.
- **OpenCV**: Biblioteca para procesamiento de imágenes.
- **NumPy**: Biblioteca para manejo de arrays y operaciones matemáticas.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias en tu entorno:

- Python 3.6 o superior
- Flask
- OpenCV
- NumPy
- Pillow (para manejar imágenes)

## Instalación y Configuración

1. **Clona el repositorio** o **descarga el código fuente**:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2. **Crea y activa un entorno virtual** (opcional pero recomendado):

    ```bash
    python -m venv env
    # En Windows
    .\env\Scripts\activate
    # En macOS/Linux
    source env/bin/activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

    Nota: Si no tienes un archivo `requirements.txt`, puedes instalar las dependencias manualmente:

    ```bash
    pip install Flask opencv-python numpy pillow
    ```

4. **Configura las carpetas necesarias**:

    Asegúrate de que la carpeta `static/uploads` existe. Esta carpeta se utiliza para almacenar las imágenes subidas y las imágenes comparadas.

5. **Ejecuta la aplicación**:

    ```bash
    python app.py
    ```

6. **Accede a la aplicación**:

    Abre tu navegador y visita `http://127.0.0.1:5000`.

## Datos del Creador

- **Nombre**: Víctor Raúl Gutiérrez Sanabria
- **Correo**: gutierrezsanabria@hotmail.com

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu contribución.
3. Realiza tus cambios y prueba.
4. Envía un pull request describiendo tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia HPND (Highly Permissive Non-Disclosure) - ver el archivo [LICENSE](LICENSE) para detalles.

