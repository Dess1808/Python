#strings
word = 'paralelepipedo'
for letter in word:
    print(letter, end=',')
print('Fim')


#list
aproved = ['Gabriel', 'Estefany', 'alex', 'Duda']
for names in aproved:
    print(names)


#position, enumerate() - return index
for position, name in enumerate(aproved):
    #start 0
    print(f'{position + 1}) {name}')


#tuple
days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
for day in days_of_the_week:
    print(f'today is {day}')


#set 
for number in (1, 4, 5, 3, 4, 8, 9, 10):
    print(number)