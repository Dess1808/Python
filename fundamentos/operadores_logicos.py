#tabela verdade do and
print(True and True)
print(True and False)
print(False and False)
print(False and True)

#tabela verdade do OR
print(True or True)
print(True or False)
print(False or False)
print(False or True)

#tabela verdade XOR, quando ha diferenca
print(True != True)
print(True != False)
print(False != False)
print(False != True)

#operador de negacao (unario)
print(not True)
print(not False)
print(not 0)
print(not 1)
print(not not -1)
print(not not True)

#cuidado!
print(True & True)
print(True | True)
print(True ^ True)

#AND Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 10

print(3 & 2)

#OR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 11

print(3 | 2)

#XOR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 01

print(3 ^ 2)


#exemplos reais
saldo = 1000
salario = 4000
despesas = 2900

saldo_positivo = saldo > 0 #nao negativo
despesas_controladas = salario - despesas >= 0.2 * salario #bateu a meta??

print(despesas_controladas)

meta = saldo_positivo and despesas_controladas

print(meta)