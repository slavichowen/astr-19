import math
import numpy

def cos(x): #returns the sin of x in radians
    return math.cos(x)
    
def sin(x): #returns the cos of x in radians
    return math.sin(x)
    
n = 1000 #amt of points
x_values = np.linspace(0,2*math.pi,n) #n amount of evenly spaced values from 0 to 2pi

sin_values = []
cos_values = []

for x in x_values:
    sin_values.append(sin(x))
    cos_values.append(cos(x))

for i in range(10):
    print(x_values[i] + " | " + sin_values[i] + " | " + cos_values[i])
