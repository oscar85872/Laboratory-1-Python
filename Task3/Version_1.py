import math

# Configuración del plano
filas, columnas = 15, 60
x_min, x_max = 0.0, 2.0
y_min, y_max = 0.0, 2.0

# Crear matriz del plano
plano = [[" "] * columnas for _ in range(filas)]

for i in range(filas):
    plano[i][0] = "│"  # Eje Y vertical

for j in range(columnas):
    plano[14][j] = "─"  # Eje X horizontal

# 2. Función raíz y = √x
for j in range(columnas):
    x = x_min + (j / (columnas - 1)) * (x_max - x_min)
    y_valor = math.sqrt(x)
    if y_min <= y_valor <= y_max:
        fila = filas - 1 - int((y_valor / y_max) * (filas - 1))
        if 0 <= fila < filas and plano[fila][j] == " ":
            plano[fila][j] = "◆"

# Imprimir el plano con valores de Y
for i in range(filas):
    y_valor = y_max - (i / (filas - 1)) * y_max
    # if y_valor.is_integer():
    #     etiqueta_y = f"{int(y_valor):2d} │"
    # else:
    #     etiqueta_y = f"{y_valor:.1f} │"
    
    #print(etiqueta_y, end="")
    #print("".join(plano[i]))
    print("".join(plano[i]))