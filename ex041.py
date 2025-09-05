from datetime import date

atual = date.today().year 
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'O atleta tem {idade} anos')

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'Classificação: {categoria}') 
