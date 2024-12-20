def validar_ip(ip):
    octetos = ip.split('.')
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        try:
            valor = int(octeto)
            if valor < 0 or valor > 255:
                return False
        except ValueError:
            return False
    return True


def validar_masc(mascara_inicial, mascara_final):
    """Converte uma máscara CIDR (sem a barra) para a representação em 4 octetos.

    Args:
        prefixo: O número de bits '1' na máscara.

    Returns:
        Uma string com a máscara em 4 octetos.
        :param mascara_inicial:
    """
    if not 0 <= mascara_inicial <= mascara_final <= 32:
        raise ValueError("As máscaras devem estar entre 0 e 32, e a inicial deve ser menor que a final.")
    # String binária com os bits '1' à esquerda e '0' à direita

    mascara_binaria = '1' * mascara_final + '0' * (32 - mascara_final)

    # Divide a string binária em octetos
    octetos = [mascara_binaria[i:i+8] for i in range(0, 32, 8)]

    # Converte cada octeto binário para decimal
    octetos_decimais = []
    for octet in octetos:
        decimal = int(octet, 2)
        octetos_decimais.append(decimal)

    # Junta os octetos decimais em uma string separada por pontos
    mascara_octetos = '.'.join(map(str, octetos_decimais))

    return mascara_octetos


def bin_to_ip(binario):
    """Converte um endereço binário para decimal com pontos."""

    octetos = []
    for i in range(0, 32, 8):
        octet_binario = binario[i:i + 8]
        octet_decimal = int(octet_binario, 2)
        octetos.append(str(octet_decimal))
    mascara_ip = '.'.join(octetos)
    return mascara_ip

def calcular_subrede(ip, mascara_inicial, mascara_final):
    """
    Calcula as informações de sub-rede para um intervalo de máscaras.

    Args:
        ip (str): Endereço IP em formato decimal com pontos.
        mascara_inicial (int): Máscara de rede inicial em notação CIDR.
        mascara_final (int): Máscara de rede final em notação CIDR.
    """

    # Converter IP para binário

    ip_binario = ''
    for x in ip.split('.'):
        num_binario = bin(int(x))[2:].zfill(8)
        ip_binario += num_binario

    for mascara in range(mascara_inicial, mascara_final + 1):
        # Máscara em binário
        mascara_binaria = '1' * mascara + '0' * (32 - mascara)

        # Calcular endereço de rede
        endereco_rede_binario = ip_binario[:mascara] + '0' * (32 - mascara)
        endereco_rede = '.'.join([str(int(endereco_rede_binario[i:i+8], 2)) for i in range(0, 32, 8)])

        # Calcular primeiro host
        primeiro_host = bin_to_ip(endereco_rede_binario[:mascara] + '0' * (31 - mascara) + '1')

        # Calcular último host
        ultimo_host = bin_to_ip(endereco_rede_binario[:mascara] + '1' * (31 - mascara) + '0')

        # Calcular endereço de broadcast
        broadcast_binario = endereco_rede_binario[:mascara] + '1' * (32 - mascara)
        broadcast = bin_to_ip(broadcast_binario)

        # Número de hosts válidos
        hosts_validos = 2**(32 - mascara) - 2

        print(f"Máscara / {mascara}")
        print(f"Endereço de Rede: {endereco_rede}")
        print(f"Primeiro Host: {primeiro_host}")
        print(f"Último Host: {ultimo_host}")
        print(f"Endereço de Broadcast: {broadcast}")
        print(f"Máscara em Binário: {mascara_binaria}")
        print(f"Número de Hosts Válidos: {hosts_validos}")


while True:
        ip = input('Digite um endereço IP: ')
        if validar_ip(ip):
            break
        else:
            print("O endereço IP é inválido, tente novamente.")


if __name__ == "__main__":
    mascara_inicial = int(input("Máscara Inicial: "))
    mascara_final = int(input("Máscara Final: "))
    mascara_octetos = validar_masc(mascara_inicial, mascara_final)
    calcular_subrede(ip, mascara_inicial, mascara_final)



