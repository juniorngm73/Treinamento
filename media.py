# Entrada de dados (convertendo para float para aceitar casas decimais)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Definição dos pesos
peso1 = 0.40  # 40%
peso2 = 0.60  # 60%

# Cálculo da média ponderada
# A fórmula é: (Nota1 * Peso1) + (Nota2 * Peso2)
media = (nota1 * peso1) + (nota2 * peso2)

print("-" * 20)
print(f"Média final: {media:.2f}")

# Estrutura condicional para verificar a aprovação
if media >= 60:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")