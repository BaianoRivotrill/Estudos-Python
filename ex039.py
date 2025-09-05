import time 
from datetime import date

atual = date.today().year 
nasc = int(input('Ano de nascimento: ')) 
idade = atual - nasc 

print('Carregando informações...')
time.sleep(2)

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

time.sleep(3)
print('Carregando conclusão...')
time.sleep(3)

if idade == 18:
    print('Você tem que se alistar IMEDIATAENTE.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18
    print(f'Já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')   