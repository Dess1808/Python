a = {1, 2, 3}
print(type(a))

a = set('coder')
print(a)

#boolan logic
print({1, 2, 3} == {2, 1, 3})

#operations
c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))
print(c1.intersection(c2))
# c1.update(c2)
print(c1)

#set test
print(c2 <= c1)
print(c2 >= c1)

#difference
print({1, 2, 3} - {2})
print(c1 - c2)

#difference with add
c1 -= {2}
print(c1)