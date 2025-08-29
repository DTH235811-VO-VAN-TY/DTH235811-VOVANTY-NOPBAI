
for i in range(4):
    for j in range(9):
        print('*',end='')
    print()

for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j ==0 or j==3:
            print('*',end='')
        else:
            print(' ',end='')
    print()
chieu_dai_tam_giac_tren = 1
for i in range(3):
    print(' ' * (4 - i) + '*', end='')
    
    if i == 1:
        print(' * * *', end='')
    elif i == 2:
        print(' * * * * * *', end='')
    print()
print(' ' * 4 + '* * *')
print(' ' * 2 + '* * * * *')
print('* * * * * * * * * * *')
for i in range(2):
    print(' ' * 8 + '* *', end='')
    print()


