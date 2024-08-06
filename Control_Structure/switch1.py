#switch simulation
def week_days(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    #get(), utilizado em um dicionario, retorna o valor da chave informada
    return days.get(day, '** invalid **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {week_days(day)}')