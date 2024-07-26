#if else test one
#chmod u+x *arquivo.py

import sys
import errno

def note_conferece(note):
    if (note <= 10.00 and note >= 9.1):
        print("A")
    elif (note <= 09.00 and note >= 8.1):
        print("A-")
    elif (note <= 08.00 and note >= 7.1):
        print("B")
    elif (note <= 07.00 and note >= 6.1):
        print("B-")
    elif (note <= 06.00 and note >= 5.1):
        print("C")
    elif (note <= 05.00 and note >= 4.1):
        print("C-")
    elif (note <= 04.00 and note >= 3.1):
        print("D")
    elif (note <= 03.00 and note >= 2.1):
        print("D-") 
    elif (note <= 02.00 and note >= 1.1):
        print("E")
    elif (note <= 01.00 and note >= 0.0):
        print("E-")
    else:
        print("invalid note")


#verificar padrao da main
if __name__ == '__main__':
    if len(sys.argv) < 2: #without parameters
        print("invalida parameters")
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric(): #is numeric? porque nao identifica ponto
        print("The value most be numeric")
        sys.exit(errno.EINVAL)


#note verification
note_conferece(float(sys.argv[1]))
