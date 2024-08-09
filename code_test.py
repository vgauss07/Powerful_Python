"""
Write a little program that asks for your name, age, and address, 
and then prints all the information you just entered. However, 
instead of placing it in a function 
called main, place it in a function called test_func. 
Then call test_func to run it.
"""

def test_func():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    add_ = input("Enter your address: ")
    print(f'Name: {name}, Age: {age}, Address: {add_}')


#test_func()

"""
Write a program that gets the radius of a sphere, calculates the volume, 
and then prints the answer. If necessary, look up the volume formula online.
"""

def radius_sphere():
    from math import pi
    radius_ = float(input("Enter the radius: "))
    volume_ = (4/3) * pi * ((radius_) ** 3)
    print(volume_)

radius_sphere()
