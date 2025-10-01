import math

WHITE_BG = "\u001b[48;2;255;255;255m"
BLACK_BG = "\u001b[40;1m"        
RESET    = "\u001b[0m"

archivo = open(r'Task4\sequence.txt', 'r')
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

print("".join('\t'*3+'|'))
for i in range(len(intervalos)):
    print(categorias[i] + '\t' + '|' + WHITE_BG + ' ' * intervalos[i] + RESET + ' '*(50-intervalos[i]) + str(porcentajes[i]) +' %' )
    print("".join('\t'*3+'|'))
print("".join('\t'*3+'_'*50))
print("".join('\t'*3 + '0' + ' '*8+ '20' + ' '*8 + '40'+ ' '*8  + '60' +' '*8+ '80' +' '*7 + '100'  ))

print('\n')
sum1 = 0
sum2 = 0 
for i in range(125):
    sum1 = sum1 + abs(numeros[i])
for j in range(125,250):
    sum2 = sum2 + abs(numeros[j])

print("First avg: {}".format(round(sum1/125,2)) + '\t'*2 + '|' + WHITE_BG + ' '*(math.floor((sum1/125)*5)) + RESET + '\t'*3 + '|' + " 48.5%")
print("Second avg: {}".format(round(sum2/125,2)) + '\t' + '|' + WHITE_BG + ' '*(math.ceil((sum2/125)*5)) + RESET + '\t'*3 + '|' + " 51.5%")
