##Pattern
for i in range(51):
    if (i<50):
        print ("\u001b[47;1m ", end=' ')
    else:
        print ("\u001b[0m", end=' ')  
for k in range(2):
    for j in range(51):
        if j == 0:
            print("\n\u001b[47;1m \u001b[0m", end='') 
        elif j < 50:
            print ("\u001b[40;1m  ", end='')
        else:
            print ("\u001b[47;1m \u001b[0m", end=' ')
print('')  
for d in range(4):
    for b in range(50):
        if b >= 0 and b<23:
            print("\u001b[47;1m  \u001b[0m", end='')
        elif b>=23 and b<28:
            print("\u001b[40;1m  ", end='')
        else:
            print ("\u001b[47;1m  ", end='')
    print('\u001b[0m')
for k in range(2):
    for j in range(51):
        if j == 0:
            print("\u001b[47;1m \u001b[0m", end='') 
        elif j < 50:
            print ("\u001b[40;1m  ", end='')
        else:
            print ("\u001b[47;1m \u001b[0m", end=' ')
    print('\u001b[0m')
for c in range(4):
    for a in range(50):
        if a>=0 and a<8:
            print("\u001b[47;1m  \u001b[0m", end='')
        elif a>=8 and a<13:
            print("\u001b[40;1m  ", end='')
        elif a>=13 and a<36:
            print("\u001b[47;1m  \u001b[0m", end='')
        elif a>=36 and a<41:
            print("\u001b[40;1m  ", end='')
        else:
            print ("\u001b[47;1m  \u001b[0m", end='')
    print('\u001b[0m')
for k in range(2):
    for j in range(51):
        if j == 0:
            print("\u001b[47;1m \u001b[0m", end='') 
        elif j < 50:
            print ("\u001b[40;1m  ", end='')
        else:
            print ("\u001b[47;1m \u001b[0m", end=' ')
    print('\u001b[0m')
for i in range(51):
    if (i<50):
        print ("\u001b[47;1m ", end=' ')
    else:
        print ("\u001b[0m", end=' ')     
