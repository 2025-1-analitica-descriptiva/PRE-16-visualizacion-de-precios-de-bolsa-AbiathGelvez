import matplotlib.pyplot as plt
import numpy as np
import os

# Crear carpeta de salida si no existe
os.makedirs("files/images", exist_ok=True)

# Datos de ejemplo (sustitúyelos con tus datos reales)
x = np.arange(10)
y = x ** 2

# Graficar
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Precios")
plt.xlabel("x")
plt.ylabel("Precio")

# Guardar
plt.savefig("files/images/precios.png")
