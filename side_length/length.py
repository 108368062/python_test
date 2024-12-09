#!/usr/bin/env python3
#use cosine formula cal result
import math
print("Given the length of two sides and an angle,\n calculate the length of the side!")
len1 = float(input("Given the first side length:"))
len2 = float(input("Given the secend side length:"))
angle = float(input("Given angle between two side:"))
angle_math = angle/180*math.pi
output_temp = pow(len1, 2)+pow(len2, 2)-2*len1*len2*math.cos(angle_math)
output_temp2 = pow(output_temp,0.5)
#print(len1)
#print(len2)
#print(angle)
#print(math.cos(angle_math))
#print(output_temp)
print("cal result:", output_temp2)