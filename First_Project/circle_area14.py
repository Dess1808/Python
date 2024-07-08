##VALIDANDO ARGUEMENTO NUMERICO

#!/usr/local/bin/python3
from math import pi
import sys #argv[]
import errno


#function
def circle(radius):
    return pi * radius ** 2


def help():
    print("Eh preciso informar o raio")
    print(f"formato correto: {sys.argv[0]} <raio>") #show corret input


if __name__ == '__main__':
    if len(sys.argv) < 2: #verification argv lenth
        help()
        sys.exit(errno.EPERM)
    #verificar!! pegando apenas numeros interios
    if not sys.argv[1].isnumeric(): #argument invalide verification
        help()
        print("o valor do raio deve ser numerico")
        sys.exit(errno.EINVAL)

        
radius = float((sys.argv[1])) #converting input
area = circle(radius) 
print('Area do circulo', area) #without f string, simple exit

    


