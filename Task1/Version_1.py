##Poland Flag
for j in range(12):
    for i in range(60):
        if (i<50):
            print ("\u001b[47;1m\u001b[31;1m ", end=' ')
        else:
            print ("\u001b[0m\u001b[0m", end=' ')    
    print(" ")
for x in range(12):
    for y in range(60):
        if (y<50):
            print ("\u001b[41;1m\u001b[33;1m ", end=' ')
        else:
            print ("\u001b[0m\u001b[0m", end=' ')    
    print(" ")

