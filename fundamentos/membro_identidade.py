#Operador de membro
lista = [1, 2, 3, 'Ana', 'Carla']

print(2 in lista)
print('Ana' not in lista)

#Operador de identidade
x = 3
y = x
z = 3

print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

#verificao em memoria, quando trabalhamos com lista
print(lista_a is lista_b) #true, mesmo local de memoria
print(lista_b is lista_c) #False, nao sao iguais (locais de momeria diferentes)
print(lista_a is not lista_c) #True, nao sao iguais (locais de momeria diferentes)
