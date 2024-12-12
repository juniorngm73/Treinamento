#  Gerando a lista através de uma função.

import random
def gerar_lista():
    while True:
        try:
            quantidade = int(input('Informe quantos números:  '))
            valor_minimo = int(input('Informe o valor inicial:'))
            valor_maximo = int(input('Informe o  valor final: '))


# Gerar  lista aleatória.
            lista = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]
            if len(lista) > 0 :
                print (True)

# Imprimir lista, sendo um numero em cada linha.
            for numero in lista:
                print(numero)

            break

        except ValueError:
            print("Valor inválido. Tente novamente.")

gerar_lista()