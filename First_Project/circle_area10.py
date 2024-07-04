#!/usr/local/bin/python3
from math import pi
import sys #argv[]


#function
def circle(radius):
    return pi * radius ** 2


if __name__ == '__main__':
    #receive radius from argv[] - terminal - without validation
    radius = float((sys.argv[1])) #converting input
    #receive return
    area = circle(radius) 
    print('Area do circulo', area) #without f string, simple exit
   
    


