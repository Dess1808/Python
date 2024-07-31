#for in dictonary

produto  = {'nome': 'Caneta Chic', 'preco': 20.00, 'importado': True, 'estoque': 500}

#keys
for key in produto:
    print(key)


#value
for value in produto.values():
    print(value)


#value and keys
for key, value in produto.items():
    print(f'{key} = {value}')


#global variable, last values 
print(key, value)