import matplotlib.pyplot as plt
import csv
X1, X2, X3 = [], [], []
Y1, Y2, Y3 = [], [], []
 
with open('dataParalela.txt', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=' ')
     
    for ROWS in plotting:
        X1.append(int(ROWS[0]))
        Y1.append(int(ROWS[1]))

with open('dataPools.txt', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=' ')
     
    for ROWS in plotting:
        X2.append(int(ROWS[0]))
        Y2.append(int(ROWS[1]))

with open('dataLineal.txt', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=' ')
     
    for ROWS in plotting:
        X3.append(int(ROWS[0]))
        Y3.append(int(ROWS[1]))

plt.plot(X1, Y1, label = 'Ejecución con hilos', color = 'red')
plt.plot(X2, Y2, label = 'Ejecución con pools', color = 'green')
plt.plot(X3, Y3, label = 'Ejecución lineal', color = 'blue')
plt.title('Gráfica de tiempo de ejecución')
plt.xlabel('Dimensiones de las matrices')
plt.ylabel('Tiempo (Microsegundos)')
plt.legend(loc = 'upper left')
plt.grid(True)

plt.rcParams['font.family'] = ['Source Han Sans TW', 'sans-serif']

plt.show()