import cv2

# Cargar la imagen
imagen = cv2.imread('th.jpeg')
cv2.imshow('ORIGINAL', imagen)
# Verificar el tamaño de la imagen
alto, ancho, _ = imagen.shape
print("Tamaño original:", alto, "x", ancho)

# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Definir factores de escala
factores = [1.5, 0.5, 0.25, 0.125]

# Aplicar interpolación de vecino más cercano, bilineal y bicúbica para cada factor
for factor in factores:
    # Escalar usando interpolación de vecino más cercano
    imagen_resized_nn = cv2.resize(imagen_gris, None, fx=factor, fy=factor, interpolation=cv2.INTER_NEAREST)
    alto, ancho = imagen_resized_nn.shape
    print("Tamaño después de escalar con factor", factor, ":", alto, "x", ancho)
    cv2.imshow('Vecino mas cercano - Factor ' + str(factor), imagen_resized_nn)
    cv2.waitKey(0)

    # Escalar usando interpolación bilineal
    imagen_resized_bilinear = cv2.resize(imagen_gris, None, fx=factor, fy=factor, interpolation=cv2.INTER_LINEAR)
    alto, ancho = imagen_resized_bilinear.shape
    print("Tamaño después de escalar con factor", factor, ":", alto, "x", ancho)
    cv2.imshow('Bilineal - Factor ' + str(factor), imagen_resized_bilinear)
    cv2.waitKey(0)

    # Escalar usando interpolación bicúbica
    imagen_resized_bicubic = cv2.resize(imagen_gris, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)
    alto, ancho = imagen_resized_bicubic.shape
    print("Tamaño después de escalar con factor", factor, ":", alto, "x", ancho)
    cv2.imshow('Bicubica - Factor ' + str(factor), imagen_resized_bicubic)
    cv2.waitKey(0)

cv2.destroyAllWindows()
