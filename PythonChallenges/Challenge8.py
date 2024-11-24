#Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything.
#The desired output should be given in kg and rounded to two decimal places.
import math


def MassOfCylinderCalculater(Radius,Height,Density):
    Volume = math.pi*Radius**2*Height
    Volume = round(Volume,2)
    Mass = Density * Volume
    Mass = round(Mass,2)
    return Mass

print(MassOfCylinderCalculater(6,3,1))


