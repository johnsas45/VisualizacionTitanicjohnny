#Escribe el siguiente codigo en el archivo visualizacion.py para importar las bibliotecas matplolib y numpy y seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#configurar el generador de numeros aleatorios
rng = np.random.RandomState(0)

#Generar un rango de valores en el eje X
x = np.linspace(0, 10, 500)

#Generear datos aleatorios y calcular la suma acumulada
y = np.cumsum(rng.randn(500, 6), axis=0)

#Graficar los datos
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

sns.set() #Aplicar estilo seaborn
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

y_val = x ** 2
plt.scatter(x, y_val, marker='s', color='g')
plt.title("grafico de dispersión")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()
