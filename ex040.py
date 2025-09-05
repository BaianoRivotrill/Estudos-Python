n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1 + n2 + n3) / 3
print(f'Tirando {n1:.1f} , {n2:.1f} e {n3:.1f}, a média do aluno é {m:.1f}')

if m >= 7:
    print('Aluno APROVADO!')  
elif m >= 5:
    print('Aluno em RECUPERAÇÃO!')
else:
    print('Aluno REPROVADO!') 