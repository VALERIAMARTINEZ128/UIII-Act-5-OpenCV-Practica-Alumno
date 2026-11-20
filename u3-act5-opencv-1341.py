import cv2

# Leer la imagen del archivo
image = cv2.imread('gato.jpg')

# Mostrar la imagen en una ventana
cv2.imshow('gato Valeria 1341', image)

# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cargar la imagen
image = cv2.imread('gato.jpg')

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Guardar la imagen en escala de grises
cv2.imwrite('gray_image.jpg', gray_image)

# Cargar la imagen
image = cv2.imread('gato.jpg')

# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200))

# Guardar la imagen redimensionada
cv2.imwrite('resized_image.jpg', resized_image)

# Mostrar la imagen redimensionada
cv2.imshow('Imagen Redimensionada Valeria 1341', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cargar la imagen
image = cv2.imread('gato.jpg')

# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2]

# Definir el centro de la imagen
center = (w // 2, h // 2)

# Matriz de rotación
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)

# Realizar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h))

# Guardar la imagen rotada
cv2.imwrite('rotated_image.jpg', rotated_image)

# Mostrar la imagen rotada
cv2.imshow('Imagen Rotada Valeria 1341', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cargar la imagen
image = cv2.imread('gato.jpg')

# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0)

# Guardar la imagen desenfocada
cv2.imwrite('blurred_image.jpg', blured_image)

# Mostrar la imagen desenfocada
cv2.imshow('Imagen Desenfocada Valeria 1341', blured_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cargar la imagen
image = cv2.imread('gato.jpg')

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100, 200)

# Guardar la imagen de bordes
cv2.imwrite('edges.jpg', edges)

# Mostrar la imagen de bordes
cv2.imshow('Bordes Canny Valeria 1341', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cargar la imagen
image = cv2.imread('gato.jpg')

# Dibujar un rectángulo
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)

# Agregar texto a la imagen
cv2.putText(image, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Guardar la imagen de salida
cv2.imwrite('output_image.jpg', image)

# Mostrar la imagen de salida
cv2.imshow('Imagen con Dibujo Valeria 1341', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cargar la imagen en escala de grises
image = cv2.imread('gato.jpg', 0)

# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Guardar la imagen umbralizada
cv2.imwrite('threshold_image.jpg', thresh_image)

# Mostrar la imagen umbralizada
cv2.imshow('Imagen Umbralizada Valeria 1341', thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cargar la imagen
image = cv2.imread('gato.jpg')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Encontrar bordes
edges = cv2.Canny(gray_image, 100, 200)

# Encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Guardar la imagen de salida con contornos
cv2.imwrite('contours_image.jpg', image)

# Mostrar la imagen con contornos
cv2.imshow('Imagen con Contornos Valeria 1341', image)
cv2.waitKey(0)
cv2.destroyAllWindows()