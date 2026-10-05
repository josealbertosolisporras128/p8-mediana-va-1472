# practica 8 Filtros, suavizado y eliminación de ruido
# jose solis NC 1472

import cv2
import os

# Obtener la carpeta donde está guardado ESTE script (codigo/)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta hacia la imagen 'loro original 1472.jpg' en la carpeta 'imagenes'
ruta_imagen = os.path.abspath(os.path.join(script_dir, "..", "imagenes", "loro original 1472.jpg"))

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Verificar la carga
if imagen is None:
    print("\nERROR: No se pudo cargar la imagen.")
    print(f"Ruta buscada: {ruta_imagen}\n")
    
    # Comprobar si existe la carpeta 'imagenes' y mostrar su contenido real
    carpeta_imagenes = os.path.abspath(os.path.join(script_dir, "..", "imagenes"))
    if os.path.exists(carpeta_imagenes):
        print(f"Archivos encontrados en '{carpeta_imagenes}':")
        print(os.listdir(carpeta_imagenes))
    else:
        print(f"La carpeta '{carpeta_imagenes}' no existe.")
    exit()

# Aplicar el filtro de mediana con ksize = 5
imagen_filtrada = cv2.medianBlur(imagen, 5)

# Mostrar ventanas con las etiquetas solicitadas
cv2.imshow("imagen original 1472", imagen)
cv2.imshow("imagen con fltro de mediana 1472", imagen_filtrada)

# Construir la ruta para guardar la imagen procesada en 'resultados'
ruta_resultado = os.path.abspath(os.path.join(script_dir, "..", "resultados", "loro_1472_mediana.jpg"))
cv2.imwrite(ruta_resultado, imagen_filtrada)

print("Filtro aplicado correctamente.")
print(f"Resultado guardado en: {ruta_resultado}")

# Esperar a que presiones cualquier tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("programa realizado por jose solis nc 1472")