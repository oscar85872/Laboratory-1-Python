import math

WHITE_BG = "\u001b[48;2;255;255;255m"
BLACK_BG = "\u001b[40;1m"        
RESET    = "\u001b[0m"

for j in range(10,0,-1):
    print('{}'.format(j) + '\t'+'|', end='')
    for i in range(1,101):
        if int(math.sqrt(i)) == j:
            print(WHITE_BG + ' ' + RESET,end='')
        else:
            print(BLACK_BG + ' ' + RESET,end='')
    print('')
print("".join('\t'+'_'*101))
print("".join('\t' + '0' + ' '*18+ '20' + ' '*18 + '40'+ ' '*18  + '60' +' '*18+ '80' +' '*18 + '100'  ))