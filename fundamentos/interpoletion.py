from string import Template

nome, idade = 'Ana', 30
#mais antiga
print('Nome: %s Idade: %d' % (nome, idade))

#python < 3.6
print('Nome: {0} Idade: {1}'.format(nome, idade))

#mais >= 3.6, string format
print(f'nome: {nome} Idade: {idade}')

#with template
s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))