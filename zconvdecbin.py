def ip_para_binario(ip_string):
    """Converte um endereço IP em formato string para sua representação binária.

    Args:
        ip_string: O endereço IP em formato string ( '192.168.1.255').

    Returns:
        Uma string com a representação binária do endereço IP, com cada octeto separado por um ponto.
    """

    octetos = ip_string.split('.')
    binario = []
    for octeto in octetos:
        binario.append(bin(int(octeto))[2:].zfill(8))  # Converte para binário e preenche com zeros à esquerda
    return '.'.join(binario)

if __name__ == "__main__":
    ip = input("Digite o endereço IP: ")
    resultado = ip_para_binario(ip)
    print("O endereço IP em binário é:", resultado)