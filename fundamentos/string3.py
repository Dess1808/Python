frase = 'Python e um linguagem excelente'
print('py' in frase)
print('ing' in frase)

#retornando o tamanho da string
print(len(frase))

#colocando toda a string em lower
print(frase.lower())

#colando em maiuscula
print(frase.upper())

#e possivel utilzar funcoes em expressoes boolean
print('py' in frase.lower())

#fazando a alteracao na variavel 
frase = frase.upper()
print(frase)

#utilzando o split, retonar substring em uma lista
print(frase.split())

#split com parametro, retirando um caracter de uma string
print(frase.split('A'))