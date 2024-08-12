def week_day(day):
    match day:
        case 2 | 3 | 4 | 5 | 6:
            return 'Day of the week'
        case 1 | 7:
            return 'weekend'
        case _:
            return '**invalid**'


if __name__ == '__main__':
    for day in range(9):
        print(f'{day}: {week_day(day)}')