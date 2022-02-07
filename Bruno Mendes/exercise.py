import math

x1 = 7886
x2 = 9953
x3 = 6250
y1 = 5954
y2 = 2425
y3 = 2108

calc_side1 = math.sqrt((x3-x1)**2 + (y3-y1)**2)

calc_side2 = math.sqrt((x2-x1)**2 + (y2-y1)**2)

calc_side3 = math.sqrt((x2-x3)**2 + (y2-y3)**2)

print(calc_side1, calc_side2, calc_side3)

s=(calc_side1 + calc_side2 + calc_side3)/2

finalarea=math.sqrt(s*(s-calc_side1)*(s-calc_side2)*(s-calc_side3))

print (s, finalarea)