def faixa_etaria(idade):
    if idade in range(0, 18):
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'Idade invalida'


if __name__ == '__main__':
    for idade in (17, 0, 45, 30, 113, -2, 100):
        print(f'{idade}: {faixa_etaria(idade)}')