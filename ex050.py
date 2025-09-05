s = 0
ct = 0

for c in (1, 7):
    n = int(input('Digite o {} valor:  '))
    if n % 2 == 0:        
        s = s + n
        ct += ct + 1
print('Você informou {ct} números PARES e a soma foi {s}')   