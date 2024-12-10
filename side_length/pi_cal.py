#!/usr/bin/env python3
#use cosine formula cal => pi
#num nead more than 3
import math
print("Given the side length of a regular polygon,\n will automatically calculate the approximate circumference of the circle!")
len1 = float(input("Given the side length of a regular polygon:"))
num = float(input("Regular polygon, number of side lengths (needs to be greater than 3):"))
angle = 360/num
angle_math = angle/180*math.pi
output_temp = pow(len1, 2)+pow(len1, 2)-2*len1*len1*math.cos(angle_math)
output_temp2 = pow(output_temp,0.5)*num
#print(len1)
#print(angle)
#print(math.cos(angle_math))
#print(output_temp)
print("cal result:", output_temp2)