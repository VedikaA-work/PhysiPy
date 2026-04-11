# -*- coding: utf-8 -*-
"""
Python program to demonstrate Newton's second law of motion 

@author: vedika_apte

"""

# Calculate Force acting on body  

def Force(m,a):
    return m*a

def calculate_force(mass):
    try:
        a = 9.8
        m = float(mass)
    
        if m<=0:
           return "Error: mass must be greater than zero"
        else:
         F = Force(m,a)
         return "Force acting on body is" , {F} , "N"

    except ValueError:
    print("Error: Enter a numeric value")

