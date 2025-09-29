WHITE_BG = "\u001b[48;2;255;255;255m"
BLACK_BG = "\u001b[40;1m"        
RESET    = "\u001b[0m"

print(WHITE_BG + ' ' * 50 + RESET )
print(WHITE_BG + ' ' + BLACK_BG + ' ' * 48 + WHITE_BG + ' ' + RESET )
for i in range(2):
    print(WHITE_BG + ' ' * 23 + BLACK_BG + ' ' * 4 + WHITE_BG + ' ' * 23 + RESET )
print(WHITE_BG + ' ' + BLACK_BG + ' '*48 + WHITE_BG + ' ' + RESET )
for i in range(2):    
    print(WHITE_BG + ' ' * 6 + BLACK_BG + ' ' * 3 + WHITE_BG + ' ' * 32 + BLACK_BG + ' ' * 3 + WHITE_BG + ' ' * 6 + RESET )
print(WHITE_BG + ' ' + BLACK_BG + ' ' * 48 + WHITE_BG + ' ' + RESET )
print(WHITE_BG + ' ' * 50 + RESET ) 