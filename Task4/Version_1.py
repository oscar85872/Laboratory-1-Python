import math
import matplotlib.pyplot as plt

archivo = open('sequence.txt', 'r')
contenido = archivo.readlines()
numeros = []

for i in range(len(contenido)):
    numeros.append(float(contenido[i]))

R = max(numeros) - min(numeros)
K = 1 + (3.322*math.log10(len(numeros)))
K = math.ceil(K)
A = R / K
intervalos = []
porcentajes = []
categorias = []
a = min(numeros)
b = min(numeros)
z = 0

for i in range(K):
    for j in range(len(numeros)):
        if numeros[j] >= a and numeros[j] < (a+A):
            z=z+1
    p = round((z/len(numeros))*100,2)
    intervalos.append(z)
    porcentajes.append(p)
    a = a+A
    z = 0
    p = 0

for i in range(K):
    categorias.append("[({}) - ({})]".format(round(b,2),round(b+A,2)))
    b = b + A

plt.figure()
plt.pie(
    porcentajes, 
    labels = categorias,
    autopct = '%1.1f%%'
    )
plt.title("Percentage ratio")
plt.show()
