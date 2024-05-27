pessoa = {'nome': 'Alberto', 'idade': 43, 'cursos': ['React', 'Python']}

#atribuicao
pessoa['idade'] = 44

#add in list
pessoa['cursos'].append('Angular')
# print(pessoa)

#del key and value with pop
pessoa.pop('nome')
print(pessoa)

#add key
pessoa.update({'idade': 28, 'sexo': 'masculino'})
print(pessoa)

#del key
del pessoa['cursos']
print(pessoa)

#clear dictionary
pessoa.clear()
print(pessoa)