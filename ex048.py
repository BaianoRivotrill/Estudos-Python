s = 0
ct = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        ct += ct + 1 
        s += s + c
print(f'A soma de todos os {ct} valores solicitados é {s}')
    