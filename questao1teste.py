ip1 = input("Digite o primeiro endereço IP: ")
ip2 = input("Digite o segundo  endereço IP: ")
mask = int(input ("Digite o tamanho da máscara de rede (em bits): "))

ip1_int = ip1.split('.')
ip10 = 0
for i, ip1_int in enumerate (ip1_int):
    pot = 3 - i
    ip10 = ip10 + int(ip1_int)* (256 ** pot)
ip10b = (f'{ip10:032b}')
print('IP 1 Bin: ', (ip10b))


ip2_int = ip2.split('.')
ip20 = 0
for i, ip2_int in enumerate (ip2_int):
    pot = 3 - i
    ip20 = ip20 + int(ip2_int)* (256 ** pot)
ip20b = (f'{ip20:032b}')

print('IP 2 Bin: ', (ip20b))


bitsHost = 32 - mask
mask10 = ((2**32) - 1) - ((2**bitsHost) - 1)
host_mask = (2**bitsHost) - 1

net1 = ip10 & mask10
net2 = ip20 & mask10
gw1 = net1 | 1
gw2 = net2 | 1
bcast1 = net1 | host_mask
bcast2 = net2 | host_mask
net1b = f"{net1:032b}"
net2b = f"{net2:032b}"
gw1b = f'{gw1:032b}'
gw2b = f'{gw2:032b}'
bc1b = f'{bcast1:032b}'
bc2b = f'{bcast2:032b}'

print (f'Net1 Bin: {net1b}')
print (f'Net2 Bin: {net2b}')
print (f'Gw 1 Bin: {gw1b}')
print (f'Gw 2 Bin: {gw2b}')
print (f'Bcast 1 Bin : {bc1b}')
print (f'Bcast 2 Bin : {bc2b}')

if net1 == net2:
    print ("Mesma Rede!!")
else:
    print ("Redes Diferentes!!")



ip_binario = bc2b

# 1. Fatiar a string binária em 4 octetos (grupos de 8 bits)

octeto_1 = ip_binario[0:8]     # 11000000
octeto_2 = ip_binario[8:16]    # 10101000
octeto_3 = ip_binario[16:24]   # 00001010
octeto_4 = ip_binario[24:32]   # 00001100

# 2. Juntar os octetos com um ponto ('.')
ip_binario_formatado = f"{octeto_1}.{octeto_2}.{octeto_3}.{octeto_4}"

print(f"IP Binário Formatado: {ip_binario_formatado}")

# Continuando do código anterior...

# Conversão de Binário para Decimal
decimal_1 = int(octeto_1, 2)
decimal_2 = int(octeto_2, 2)
decimal_3 = int(octeto_3, 2)
decimal_4 = int(octeto_4, 2)

# Juntar os valores decimais com um ponto ('.')
ip_decimal = f"{decimal_1}.{decimal_2}.{decimal_3}.{decimal_4}"

print(f"IP Decimal: {ip_decimal}")