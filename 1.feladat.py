#Write a program that stores 3 sides of a cuboid as variables (doubles)
#The program should write the surface area and volume of the cuboid.
#Set the 3 sides to 10.4, 13.5, 8.2 and your program should
#produce the following output:
#Surface Area: 672.76
#Volume: 1151.28

l = float(10.4)
w = float(13.5)
h = float(8.2)
a = l*w*h
v = 2*(w*l+h*l+h*w)
print(f"A felszín: {a}, a térfogat: {v}")

#Print the Body mass index (BMI) based on these values.
#Example:
#mass_in_kg = 81.2
#height_in_m = 1.78

import math
m = 1.60
s = 60
bmi = s / math.pow(m,2)
eredmeny = round(bmi,2)
print(f"BMI: {eredmeny}")

#Write a program that checks if a given year is a leap year or not.
#Leap years:
#2000, 2004, 1904, 2024, 1600
#Not leap years:
#1900, 1929, 1933, 2023, 1867

ev = int(input("Adjon meg egy évet!"))
if(ev%4==0) and (ev%100 == 0) and(ev%400 == 0):
    print ("Szökőév")