peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc <= 25:
    print('Você está na faixa do PESO NORMAL.')
elif imc <= 30:
    print('Você está na faixa de SOBRE PESO')
elif imc <= 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')