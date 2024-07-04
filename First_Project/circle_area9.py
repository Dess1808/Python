#!/usr/local/bin/python3
from math import pi


#function
def circle(radius):
    return pi * radius ** 2


if __name__ == '__main__':
    radius = float(input("radius: "))
    area = circle(radius) #receive return
    print('Area do circulo', area) #without f string, simple exit
   
    


