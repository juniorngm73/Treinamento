# Tabuada
# Solicita o número ao usuário
num = int(input("Digite um número para ver sua tabuada: "))

# Imprime a tabuada usando um loop for
for n in range(1, 11):
    resultado = num * n
    print(f"{num} x {n} = {resultado}")
