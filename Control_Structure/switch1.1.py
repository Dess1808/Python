def week_day(day):
    match day:
        case 1:
            return 'Domingo'
        case 2:
            return 'Segunda'
        case 3: 
            return 'Terca'
        case 4:
            return 'Quarta'
        case 5:
            return 'Quinta'
        case 6:
            return 'Sexta'
        case 7:
            return 'Sabado'
        case _:
            return '**invalido**'


if __name__ == '__main__':
    for day in range(8):
        print(f'{day}: {week_day(day)}')
