import math

filas = 15 
columnas = 60

matriz = [[' '] * columnas for _ in range(filas)]

for i in range(filas):
    matriz[i][0] = "\u2502" 

for j in range(columnas):
    matriz[14][j] = "\u2500"  

for i in range(columnas):
    x = 0.0 + (i/(columnas-1))*(2.0)
    y = math.sqrt(x)
    if 0.0 <= y and y <= 1.5:
        fila = filas - 1 - int((y / 1.5) * (filas - 1))
        if 0 <= fila and fila < filas and matriz[fila][i] == " ":
            matriz[fila][i] = "*"

for i in range(filas):
    print("".join(matriz[i]))
