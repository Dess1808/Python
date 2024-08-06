#se day for igual a 1 ou 7 - fim de semana, diferente, dia da semana
#solution: 
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
    return days.get(day)


if __name__ == '__main__':
    for day in range(0, 9):
        if day == 1 or day == 7:
            print(f'{day}: {week_days(day)}, weekend')
        elif day <= 0 or day >= 8:
            print(f'{day}: ** Invalid day **')
        else:
            print(f'{day}: {week_days(day)}, day of the week')
            
            
