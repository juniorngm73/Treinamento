ip1 = input("Digite o primeiro endereço IP: ")
ip2 = input("Digite o segundo endereço IP: ")
mask = int(input ("Digite o tamanho da máscara de rede (em bits): "))

ip1_int = ip1.split('.')
ip10 = 0
for i, ip1_int in enumerate (ip1_int):
    pot = 3 - i
    ip10 = ip10 + int(ip1_int)* (256 ** pot)



ip2_int = ip2.split('.')
ip20 = 0
for i, ip2_int in enumerate (ip2_int):
    pot = 3 - i
    ip20 = ip20 + int(ip2_int)* (256 ** pot)


bitsHost = 32 - mask
mask10 = ((2**32) - 1) - ((2**bitsHost) - 1)
host_mask = (2**bitsHost) - 1

net1 = ip10 & mask10
net2 = ip20 & mask10
gw1 = net1 | 1
gw2 = net2 | 1
bcast1 = net1 | host_mask
bcast2 = net2 | host_mask



if net1 == net2:
    print ("Mesma Rede!!!")
else:
    print ("Redes Diferentes!!!")