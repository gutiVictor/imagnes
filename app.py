from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)

def find_similar_images(uploaded_image_path):
    image_dir = 'static/uploads'
    similar_images = []

    # Cargar la imagen subida
    uploaded_img = cv2.imread(uploaded_image_path, cv2.IMREAD_GRAYSCALE)
    uploaded_img = cv2.resize(uploaded_img, (100, 100))  # Redimensionar para comparación

    for filename in os.listdir(image_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(image_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (100, 100))  # Redimensionar para comparación

            # Comparar la imagen
            diff = cv2.absdiff(uploaded_img, img)
            non_zero_count = np.count_nonzero(diff)

            # Umbral para considerar imágenes como similares
            if non_zero_count < 8000:  # Ajusta este valor según sea necesario
                similar_images.append(filename)

    return similar_images

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            file_path = f"static/uploads/temp_image.png"
            uploaded_file.save(file_path)
            similar_images = find_similar_images(file_path)
            if similar_images:
                return render_template('index.html', similar_images=similar_images)
            else:
                return "Imagen subida y no se encontraron imágenes similares."
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
