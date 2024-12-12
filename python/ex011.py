# Pintura de Parede

l = int(input('Digite a largura da parede (m):'))
a = int(input('Digite a altura  da parede (m):'))
s = l*a
# cada litro de tinta pinta 2 m²
tinta = s/2
print(f'A parede possui {s} m² de Área.')
print(f'Necessita de {tinta} lts de tinta para a pintura.')
