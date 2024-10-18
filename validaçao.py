def validar_ip(ip):
    try:
        octetos = ip.split('.')
        if len(octetos) != 4:
            return False

        for octeto in octetos:
            if  not octeto.isdigit() or not 0 <= int(octeto) <= 255:
                return False

        return True
    except ValueError:
        print(f'O endereço IP contém caracteres inválidos.')
        return False

while True:
    ip = input(' Digite um endereço IP: ')
    if validar_ip(ip):
        print('O endereço IP é válido.')
        break
    else:
        print("O endereço IP é inválido, tente novamente.")