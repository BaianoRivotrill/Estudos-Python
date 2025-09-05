casa = float(input('Valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Quantos anos de financiamento: ')) 

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos')
print(f'a prestação será de R${prestacao:.2f}')  

if prestacao <= minimo:
    print(f'Empréstimo aprovado! O valor da prestação mensal será de R${prestacao:.2f}') 
else:
    print(f'Emprestimo negado! O valor da prestação excede 30% do seu salário')


  