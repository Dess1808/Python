#!/usr/local/bin/python3
from math import pi


#function
def circle(radius):
    print(f'area of circle: {pi * radius ** 2}')


if __name__ == '__main__':
    radius = float(input("radius: "))
    circle(radius) #call function
   
    


