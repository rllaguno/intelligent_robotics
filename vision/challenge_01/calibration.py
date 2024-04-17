import numpy as np
import cv2

# Tamaño del patrón de calibración
pattern_size = (3, 3)  # Filas x Columnas de esquinas interiores

# Generar puntos de calibración en el patrón
objp = np.zeros((np.prod(pattern_size), 3), dtype=np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

# Lista para almacenar puntos de calibración detectados en imágenes
objpoints = []  # 3D puntos en el mundo real
imgpoints = []  # 2D puntos en la imagen (plano)

# Leer imágenes de la cámara o cargar imágenes de archivo
img = cv2.imread('calib2.png')  # Cambia 'sample_image.jpg' al nombre de tu archivo de imagen

# Encuentra las esquinas del patrón en las imágenes
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

# Si se encontraron las esquinas, agregar puntos de calibración
if ret == True:
    objpoints.append(objp)
    imgpoints.append(corners)

    # Dibujar y mostrar las esquinas
    img = cv2.drawChessboardCorners(img, pattern_size, corners, ret)
    cv2.imshow('img', img)
    cv2.waitKey(0)

# Calibrar la cámara
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Guardar la matriz de calibración y los coeficientes de distorsión si es necesario
# Esto puede ser útil para usar la cámara calibrada en otras aplicaciones
# np.savez('calibration_data.npz', mtx=mtx, dist=dist)

# Deshacer la distorsión en una imagen de ejemplo
undistorted_img = cv2.undistort(img, mtx, dist, None, mtx)

# Mostrar imágenes
cv2.imshow('Original Image', img)
cv2.imshow('Undistorted Image', undistorted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()