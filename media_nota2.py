# Entrada da primeira nota
nota1 = float(input("Digite a Nota 1: "))

# Meta de aprovação
media_desejada = 60

# Cálculo da nota necessária
# Isolamos a nota2 na equação: (nota1 * 0.4 + nota2 * 0.6 = 60)
nota2_necessaria = (media_desejada - (nota1 * 0.4)) / 0.6

print("-" * 30)
if nota2_necessaria <= 0:
    print(f"Você já atingiu a média! Nota 2 necessária: 0")
elif nota2_necessaria > 100:
    print(f"Nota necessária: {nota2_necessaria:.2f}")
    print("Atenção: Matematicamente impossível atingir a média nesta prova (acima de 100).")
else:
    print(f"Para ser aprovado com média 60, você precisa tirar {nota2_necessaria:.2f} na Nota 2.")