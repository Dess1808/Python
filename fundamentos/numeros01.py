
# dir(int)
# dir(float)

a = 5
b = 2.5

print(a / b)
print(a + b)
print(a * b)

print(type(a))
print(type(b))
print(a - b)

print(b.is_integer())
print(5.0.is_integer())

# #voce pode utilizar funcoees internas dos tipos, 
# basta verificar atraves do dir() passando como 
# parametros o item que deseja

print(int.__add__(2, 3))
print(2 + 3) #mesma coisa


#two molds
print((-2).__abs__())
print(abs(-2))

print((-3.6).__abs__())
print(abs(-3.6))




