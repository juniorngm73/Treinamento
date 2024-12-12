n1 = float(input('Digite a nota 1 : '))
n2 = float(input('Digite a nota 2 : '))
media = (n1*4 + n2*6)/10

if media >= 60:
    print('aprovado', media)
else:
    print('Reprovado',media)
