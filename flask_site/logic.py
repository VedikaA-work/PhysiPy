# -*- coding: utf-8 -*-
"""
Python program to demonstrate Newton's second law of motion 

@author: vedika_apte

"""

# Calculate Force acting on body  

def Force(m,a):
    return m*a

try:
    mass = input("Enter mass in kg(kg):")
    accl = 9.8
    
    m = float(mass)
    a = float(accl)
    
    if m==0:
        print("Error: mass cannot be zero")
    else:
        F = Force(m,a)
        print("Force acting on body is" , F , "N")

except:
    print("Error: Enter a numeric value")
    
Force(m,a)
