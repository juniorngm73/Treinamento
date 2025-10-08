def validar_ip(entrada):  # Nome da função é 'validar_ip' e o parâmetro é 'entrada'
    """
    Lê um IP do usuário, repetindo a solicitação (entrada) até que
    o IP seja válido (formato IPv4: quatro octetos entre 0 e 255).
    """
    while True:
        ip = input(entrada)

        octetos = ip.split('.')

        # 1. Checa o número de octetos
        if len(octetos) != 4:
            print(f"ERRO: O IP '{ip}' é INVÁLIDO. Tente Novamente.")
            continue

        # 2. Checa o valor de cada octeto
        is_valid = True
        for octeto in octetos:
            try:
                valor = int(octeto)
                if valor < 0 or valor > 255:
                    is_valid = False
                    break
            except ValueError:
                is_valid = False
                break

        # 3. Retorna o IP se for válido, ou exibe erro e repete
        if is_valid:
            return ip  # IP válido: retorna e encerra a função
        else:
            print(
                f"ERRO: O IP '{ip}' é INVÁLIDO. Tente Novamente.")


#  CHAMANDO  A FUNÇÃO
# Chamada 1: Chama 'validar_ip' e a mensagem passada é o valor do parâmetro 'entrada'
ip1 = validar_ip('Digite o PRIMEIRO IP válido: ')

# Chamada 2:Chama 'validar_ip' e a mensagem passada é o valor do parâmetro 'entrada'
ip2 = validar_ip('Digite o SEGUNDO IP válido: ')
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


if net1 == net2:
    print ("Mesma Rede!!!")
else:
    print ("Redes Diferentes!!!")