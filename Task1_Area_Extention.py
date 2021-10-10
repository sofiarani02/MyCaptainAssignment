print("_________Area Of Circle________")
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

print("\n________Extention of File_________")
filename = input("Input the Filename: ")
f = filename.split(".")
if(f[-1]=="py"):
    print ("The extension of the file is : Python")
else:
    print ("The extension of the file is : ",f[-1])
