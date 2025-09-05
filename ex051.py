p = int(input('Primeira razão: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r

for c in range(p, d + r, r):
    print(c, end=' ->')
print('ACABOU!')    
    