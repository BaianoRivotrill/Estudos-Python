pa = 'palíndromo'

f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = j[::-1]

print('O inverso de {j} é {i}')
if i == j:
    print(f'Temos um {pa}')
else:
    print(f'A frase digitada não é um {pa}')
    