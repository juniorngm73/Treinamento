# Aumento de salario

salario = float(input('Digite o valor do salário:'))
aumento = float(input('Digite o Percentual de aumento:'))/100

novo_salario = salario + (salario * aumento)
print(f'Você obteve aumento de {aumento*100}%, Seu Salário agora é R$ {novo_salario} reais')

