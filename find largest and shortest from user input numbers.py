# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
largest = None
smallest = None

while True :
    num = input("Enter a number:")
    if num == 'done':
        break
    try:
        n = float(num)
    except:
        print("Invalid input")
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
    if largest is None:
        largest = n
    elif n > largest:
        largest = n
print("Maximum is", largest)
print("Minimum is", smallest)

    
    

