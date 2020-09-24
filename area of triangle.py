import math
a = float(input('enter the side 1:'))
b = float(input('enter the side 2:'))
c = float(input('enter the side 3:'))
s = (a+b+c)/2
print(s)
area = math.sqrt(s * (s - b) * (s - c))
print("the area of triangle", area)
